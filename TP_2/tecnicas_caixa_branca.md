# Técnicas de Caixa Branca — Como e Porquê

---

## O que fizemos nos Sprints 1 e 2 (caixa preta)

Nos sprints anteriores testámos o sistema **de fora para dentro**: dávamos uma entrada, verificávamos a saída, sem olhar para o código.

- **Particionamento de Equivalência (PE):** agrupamos entradas semelhantes em classes e testamos um representante de cada. Ex: password vazia, password correta, password nula — três classes, três testes, em vez de testar todas as passwords possíveis.
- **Análise de Valores Limite (VL):** testamos exactamente nos limites de um intervalo e logo fora deles. Ex: temperatura aceite em [18, 28] → testamos 17, 18, 23, 28 e 29.

Estas técnicas não precisam de ver o código — só precisam de saber o que a função deve fazer.

---

## O problema no Sprint 3

Algumas funções do Sprint 3 têm um `if` com **várias condições ao mesmo tempo**:

```python
# alert_service.classify_alert — código real simplificado
if not sensor_ok:
    return None
if temp > 28 and humidity < 40:
    return "Crítico"
if temp > 28 or humidity < 40:
    return "Aviso"
return None
```

Este `if` depende de **três coisas ao mesmo tempo**: a temperatura, a humidade e o sensor. Com PE e VL testaríamos cada uma isolada — mas e se a combinação entre elas criar um comportamento inesperado? Por exemplo: sensor activo + temperatura alta + humidade normal → "Aviso". Mas sensor activo + temperatura alta + humidade baixa → "Crítico". São resultados diferentes para a mesma temperatura.

Para cobrir estas situações usamos **técnicas de caixa branca** — olhamos para dentro do código e desenhamos testes a partir da lógica das condições.

---

## O que são C1, C2, C3

São apenas **nomes** que damos a cada parte do `if`. Em vez de escrever a condição completa repetidamente, chamamos-lhe C1, C2, C3.

Para `classify_alert`:

```
C1 = (temp > 28)          ← a temperatura está acima do limite?
C2 = (humidity < 40)      ← a humidade está abaixo do limite?
C3 = sensor_ok            ← o sensor está a funcionar?
```

A decisão completa é: **(C1 OR C2) AND C3**
→ só gera alerta se pelo menos uma leitura estiver fora dos limites **e** o sensor estiver activo.

---

## O que são T e F

Simples: **T = True (verdadeiro)**, **F = False (falso)**.

Nas tabelas, em vez de escrever "temperatura está acima do limite = sim", escrevemos C1 = T.

---

## O que é a Cobertura de Condições Múltiplas

A ideia é testar **todas as combinações possíveis** de T e F para C1, C2 e C3.

Com 3 condições, cada uma podendo ser T ou F, há **2 × 2 × 2 = 8 combinações**:

| # | C1 (temp alta) | C2 (hum baixa) | C3 (sensor ok) | O que acontece  | Teste  |
|---|----------------|----------------|----------------|-----------------|--------|
| 1 | F              | F              | F              | Nenhum alerta   | TU-57  |
| 2 | F              | F              | T              | Nenhum alerta   | TU-58  |
| 3 | F              | T              | F              | Nenhum alerta   | TU-59  |
| 4 | F              | T              | T              | **"Aviso"**     | TU-60  |
| 5 | T              | F              | F              | Nenhum alerta   | TU-61  |
| 6 | T              | F              | T              | **"Aviso"**     | TU-62  |
| 7 | T              | T              | F              | Nenhum alerta   | TU-63  |
| 8 | T              | T              | T              | **"Crítico"**   | TU-64  |

Os testes TU-57 a TU-64 executam exactamente estas 8 linhas, garantindo que **nenhuma combinação ficou por testar**.

---

## O que é MC/DC

MC/DC (Modified Condition / Decision Coverage) é uma versão mais eficiente. Em vez de testar as 8 combinações, pergunta: **"consigo provar que cada condição individual importa?"**

Uma condição "importa" se existe um caso onde mudá-la sozinha (de F para T ou de T para F), mantendo tudo o resto igual, **muda o resultado final**.

### Exemplo concreto para C3 (sensor_ok)

Olhamos para os casos #3 e #4 da tabela:

| # | C1 | C2 | C3          | Resultado      |
|---|----|----|-------------|----------------|
| 3 | F  | T  | **F**       | Nenhum alerta  |
| 4 | F  | T  | **T**       | "Aviso"        |

C1 e C2 são iguais nos dois casos. Só C3 muda (F → T). E o resultado muda (None → "Aviso"). **Portanto C3 é independente — provámos que ela por si só afecta o resultado.**

Fazemos o mesmo para C1 (casos #2 e #6) e para C2 (casos #2 e #4).

O resultado: bastam **4 testes** para satisfazer MC/DC em vez dos 8 da cobertura completa. No projeto usámos os 8 na mesma (cobertura total), que é ainda mais rigorosa.

---

## Resumo: os 3 casos onde aplicámos estas técnicas no Sprint 3

### `classify_alert` — TU-57 a TU-64
Decisão: **(C1 OR C2) AND C3** — temperatura, humidade e sensor.
8 combinações testadas, cobrindo todos os caminhos possíveis.

**Pares MC/DC (prova que cada condição importa):**

| Condição | Casos comparados | O que muda        | Resultado muda de        |
|----------|-----------------|-------------------|--------------------------|
| C1 (temp)   | TU-58 vs TU-62 | só C1: F → T     | `None` → `"Aviso"`      |
| C2 (hum)    | TU-58 vs TU-60 | só C2: F → T     | `None` → `"Aviso"`      |
| C3 (sensor) | TU-60 vs TU-59 | só C3: T → F     | `"Aviso"` → `None`      |

---

### `transition_batch_state` — TU-65 a TU-70
Decide o novo estado de um lote ao ser fechado.

```
C1 = (estado actual é "ativo")
C2 = (tem perdas registadas)
C3 = (data de conclusão definida)
```

| # | C1 | C2 | C3 | Resultado           | Teste  |
|---|----|----|----|--------------------|--------|
| 1 | T  | F  | T  | `"concluído"`      | TU-65  |
| 2 | T  | T  | T  | `"comprometido"`   | TU-66  |
| 3 | T  | F  | F  | Erro               | TU-67  |
| 4 | F  | F  | T  | Erro (já fechado)  | TU-68  |
| 5 | F  | T  | T  | Erro (já fechado)  | TU-69  |
| 6 | F  | F  | T  | Erro (estado inválido) | TU-70 |

**Pares MC/DC:**

| Condição | Casos comparados | O que muda    | Resultado muda de                   |
|----------|-----------------|---------------|-------------------------------------|
| C2 (perdas)    | TU-65 vs TU-66 | só C2: F → T | `"concluído"` → `"comprometido"`  |
| C3 (end_date)  | TU-65 vs TU-67 | só C3: T → F | `"concluído"` → Erro               |
| C1 (estado)    | TU-65 vs TU-68 | só C1: T → F | `"concluído"` → Erro               |

---

### `decide_automation` — TU-76 a TU-79
Decide se uma acção de automação é executada, sugerida ou ignorada.

```
C1 = (modo == "Automático")
C2 = (regra está activa)
C3 = (medição é recente)
```

Aqui usámos directamente o subconjunto MC/DC mínimo (4 testes chegam para provar independência das 3 condições):

| # | C1 | C2 | C3 | Resultado     | Teste  |
|---|----|----|----|---------------|--------|
| 1 | T  | T  | T  | `"executada"` | TU-76  |
| 2 | F  | T  | T  | `"sugerida"`  | TU-77  |
| 3 | T  | F  | T  | `"ignorada"`  | TU-78  |
| 4 | F  | T  | F  | `"ignorada"`  | TU-79  |

**Pares MC/DC:**

| Condição | Casos comparados | O que muda    | Resultado muda de                 |
|----------|-----------------|---------------|-----------------------------------|
| C1 (modo)   | TU-76 vs TU-77 | só C1: T → F | `"executada"` → `"sugerida"`    |
| C2 (regra)  | TU-76 vs TU-78 | só C2: T → F | `"executada"` → `"ignorada"`    |
| C3 (medição)| TU-77 vs TU-79 | só C3: T → F | `"sugerida"` → `"ignorada"`     |

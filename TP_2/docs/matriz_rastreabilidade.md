# Matriz de Rastreabilidade

## Sprint 1 — Autenticação (`/auth`)

| ID | Requisito / Regra | Endpoint | Nível | Técnica | Resultado Esperado | Pré-condições |
| --- | --- | --- | --- | --- | --- | --- |
| TU-01 | RN-01: login com credenciais corretas | (validador de credenciais) | Unidade | Particionamento de Equivalência (username e password válidos) | Devolve os dados do utilizador sem a password. | Utilizadores predefinidos em memória (tecnico, responsavel, admin). |
| TU-02 | RN-02: login com password errada | (validador de credenciais) | Unidade | Particionamento de Equivalência (password não corresponde) | Não autentica (devolve vazio); equivale a 401 na API. | Utilizadores predefinidos em memória (tecnico, responsavel, admin). |
| TU-03 | RN-03: password não pode ser vazia | (validador de credenciais) | Unidade | Particionamento de Equivalência (password = "") | Recusa o pedido como entrada inválida; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-04 | RN-04: password não pode ser nula | (validador de credenciais) | Unidade | Particionamento de Equivalência (password = null) | Recusa o pedido como entrada inválida; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-05 | RN-05: password não pode ser só espaços | (validador de credenciais) | Unidade | Particionamento de Equivalência (password = "   ") | Recusa o pedido como entrada inválida; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-06 | RN-06: password não pode exceder o tamanho máximo | (validador de credenciais) | Unidade | Particionamento de Equivalência (password com 129+ caracteres) | Recusa o pedido como entrada inválida; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-07 | RN-07: password não pode ter caracteres proibidos | (validador de credenciais) | Unidade | Particionamento de Equivalência (password = "pass;drop") | Recusa o pedido como entrada inválida; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-08 | RN-08: login com utilizador inexistente | (validador de credenciais) | Unidade | Particionamento de Equivalência (username desconhecido) | Não autentica (devolve vazio); equivale a 401 na API. | Utilizadores predefinidos em memória (tecnico, responsavel, admin). |
| TU-09 | RN-09: login com utilizador inexistente e password errada | (validador de credenciais) | Unidade | Particionamento de Equivalência (username e password inválidos) | Não autentica (devolve vazio); equivale a 401 na API. | Utilizadores predefinidos em memória (tecnico, responsavel, admin). |
| TU-10 | RN-10: username não pode ser vazio | (validador de credenciais) | Unidade | Particionamento de Equivalência (username = "") | Recusa o pedido como entrada inválida; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-11 | RN-11: username e password não podem ser ambos vazios | (validador de credenciais) | Unidade | Particionamento de Equivalência (username = "", password = "") | Recusa o pedido como entrada inválida; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-12 | RN-12: username não pode ser nulo | (validador de credenciais) | Unidade | Particionamento de Equivalência (username = null) | Recusa o pedido como entrada inválida; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-13 | RN-13: username e password não podem ser ambos nulos | (validador de credenciais) | Unidade | Particionamento de Equivalência (username = null, password = null) | Recusa o pedido como entrada inválida; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-14 | RN-14: username não pode ser só espaços | (validador de credenciais) | Unidade | Particionamento de Equivalência (username = "   ") | Recusa o pedido como entrada inválida; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-15 | RN-15: username não pode exceder o tamanho máximo | (validador de credenciais) | Unidade | Particionamento de Equivalência (username com 129+ caracteres) | Recusa o pedido como entrada inválida; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-16 | RN-16: username não pode ter caracteres proibidos | (validador de credenciais) | Unidade | Particionamento de Equivalência (username = "@dm!n") | Recusa o pedido como entrada inválida; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-17 | RN-17: emissão de token de acesso | (emissor de tokens JWT) | Unidade | Particionamento de Equivalência (utilizador válido, tipo access) | Emite um JWT de acesso com id, username, perfil, tipo e validade. | Utilizador admin autenticado em memória. |
| TU-18 | RN-18: emissão de token de renovação | (emissor de tokens JWT) | Unidade | Particionamento de Equivalência (utilizador válido, tipo refresh) | Emite um JWT de renovação com id, username, perfil, tipo e validade. | Utilizador admin autenticado em memória. |
| TU-19 | RN-19: não emite token sem utilizador | (emissor de tokens JWT) | Unidade | Particionamento de Equivalência (utilizador = null) | Recusa a emissão; equivale a erro de pedido. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-20 | RN-20: não emite token de tipo desconhecido | (emissor de tokens JWT) | Unidade | Particionamento de Equivalência (tipo fora de {access, refresh}) | Recusa a emissão; equivale a erro de pedido. | Utilizador admin autenticado em memória. |
| TU-21 | RN-21: aceita token de acesso válido | (validador de tokens JWT) | Unidade | Particionamento de Equivalência (token válido e íntegro) | Descodifica e devolve o conteúdo do token. | Token de acesso admin gerado. |
| TU-22 | RN-22: recusa token de acesso onde se espera renovação | (validador de tokens JWT) | Unidade | Particionamento de Equivalência (tipo access onde se espera refresh) | Recusa o token; equivale a 401 na API. | Token de acesso admin gerado. |
| TU-23 | RN-23: recusa token malformado | (validador de tokens JWT) | Unidade | Particionamento de Equivalência (string que não é um JWT) | Recusa o token; equivale a 401 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-24 | RN-24: recusa token vazio | (validador de tokens JWT) | Unidade | Particionamento de Equivalência (token = "") | Recusa o token; equivale a 401 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-25 | RN-25: recusa token nulo | (validador de tokens JWT) | Unidade | Particionamento de Equivalência (token = null) | Recusa o token; equivale a 401 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-26 | RN-26: recusa token com assinatura adulterada | (validador de tokens JWT) | Unidade | Particionamento de Equivalência (assinatura alterada) | Recusa o token; equivale a 401 na API. | Token válido gerado e últimos caracteres da assinatura trocados. |
| TU-27 | RN-27: recusa token expirado | (validador de tokens JWT) | Unidade | Particionamento de Equivalência (validade no passado) | Recusa o token; equivale a 401 na API. | Token criado com expiração no passado. |
| TU-28 | RN-28: renova a partir de token de renovação válido | (renovador de tokens JWT) | Unidade | Particionamento de Equivalência (refresh válido e registado) | Devolve um novo par de tokens (acesso + renovação). | Token de renovação admin válido e registado em memória. |
| TU-29 | RN-29: recusa renovação com token expirado | (renovador de tokens JWT) | Unidade | Particionamento de Equivalência (refresh expirado) | Recusa a renovação; equivale a 401 na API. | Token de renovação com validade no passado. |
| TU-30 | RN-30: recusa renovação com token malformado | (renovador de tokens JWT) | Unidade | Particionamento de Equivalência (refresh malformado) | Recusa a renovação; equivale a 401 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-31 | RN-31: recusa renovação com token vazio | (renovador de tokens JWT) | Unidade | Particionamento de Equivalência (refresh = "") | Recusa a renovação; equivale a 401 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-32 | RN-32: recusa renovação com token nulo | (renovador de tokens JWT) | Unidade | Particionamento de Equivalência (refresh = null) | Recusa a renovação; equivale a 401 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-33 | RN-33: recusa renovação com token válido mas não registado | (renovador de tokens JWT) | Unidade | Particionamento de Equivalência (refresh válido fora do registo) | Recusa a renovação; equivale a 401 na API. | Token de renovação gerado e removido do registo em memória. |

## Sprint 2 — Importação de Ervas e Criação de Planos (`/herbs`, `/plans`)

| ID | Requisito / Regra | Endpoint | Nível | Técnica | Resultado Esperado | Pré-condições |
| --- | --- | --- | --- | --- | --- | --- |
| TU-34 | RN-34: importa ervas com campos opcionais vazios | (importador de catálogo CSV) | Unidade | Particionamento de Equivalência (linhas válidas, família/descrição em branco) | Importa as 2 ervas; catálogo fica com 2 entradas e 0 falhas. | Catálogo vazio. Ficheiro CSV com nome preenchido e campos opcionais em branco. |
| TU-35 | RN-35: rejeita importação de ficheiro vazio | (importador de catálogo CSV) | Unidade | Particionamento de Equivalência (CSV vazio) | Rejeita com mensagem de ficheiro vazio; equivale a 400 na API. | Catálogo vazio. Conteúdo do CSV é uma string vazia. |
| TU-36 | RN-36: reimportar as mesmas ervas cria duplicados | (importador de catálogo CSV) | Unidade | Particionamento de Equivalência (nomes repetidos do catálogo) | Importa as 3 linhas; catálogo passa a 5 entradas (Manjericão e Tomilho repetidos). | Catálogo com 2 ervas (Manjericão, Tomilho). CSV reimporta-as + Orégão nova. |
| TU-37 | RN-37: importar ervas novas não duplica as existentes | (importador de catálogo CSV) | Unidade | Particionamento de Equivalência (nomes distintos dos existentes) | Importa as 2 novas; catálogo passa a 4 entradas sem duplicar as anteriores. | Catálogo com 2 ervas (Manjericão, Tomilho). CSV importa Orégão e Menta. |
| TU-38 | RN-38: rejeita erva com nome de tipo errado | (validador de ervas) | Unidade | Particionamento de Equivalência (nome = inteiro em vez de texto) | Rejeita a erva como entrada inválida; equivale a 400 na API. | Nenhuma. Payload com nome numérico (123). |
| TU-39 | RN-39: temperatura abaixo do mínimo | (validador de planos de cultivo) | Unidade | Valores Limite (temperatura = 17 °C, abaixo de 18) | Validador rejeita o plano. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-40 | RN-40: temperatura acima do máximo | (validador de planos de cultivo) | Unidade | Valores Limite (temperatura = 29 °C, acima de 28) | Validador rejeita o plano. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-41 | RN-41: temperatura no limite inferior | (validador de planos de cultivo) | Unidade | Valores Limite (temperatura = 18 °C, limite inferior exato) | Validador aceita o plano. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-42 | RN-42: temperatura no limite superior | (validador de planos de cultivo) | Unidade | Valores Limite (temperatura = 28 °C, limite superior exato) | Validador aceita o plano. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-43 | RN-43: temperatura num valor interior | (validador de planos de cultivo) | Unidade | Valores Limite (temperatura = 23 °C, valor nominal) | Validador aceita o plano. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-44 | RN-44: humidade abaixo do mínimo | (validador de planos de cultivo) | Unidade | Valores Limite (humidade = 39 %, abaixo de 40) | Validador rejeita o plano. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-45 | RN-45: humidade acima do máximo | (validador de planos de cultivo) | Unidade | Valores Limite (humidade = 81 %, acima de 80) | Validador rejeita o plano. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-46 | RN-46: humidade no limite inferior | (validador de planos de cultivo) | Unidade | Valores Limite (humidade = 40 %, limite inferior exato) | Validador aceita o plano. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-47 | RN-47: humidade no limite superior | (validador de planos de cultivo) | Unidade | Valores Limite (humidade = 80 %, limite superior exato) | Validador aceita o plano. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-48 | RN-48: humidade num valor interior | (validador de planos de cultivo) | Unidade | Valores Limite (humidade = 64 %, valor nominal) | Validador aceita o plano. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-49 | RN-49: luminosidade abaixo do mínimo | (validador de planos de cultivo) | Unidade | Valores Limite (luminosidade = 4999 lux, abaixo de 5000) | Validador rejeita o plano. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-50 | RN-50: luminosidade acima do máximo | (validador de planos de cultivo) | Unidade | Valores Limite (luminosidade = 25001 lux, acima de 25000) | Validador rejeita o plano. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-51 | RN-51: luminosidade no limite inferior | (validador de planos de cultivo) | Unidade | Valores Limite (luminosidade = 5000 lux, limite inferior exato) | Validador aceita o plano. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-52 | RN-52: luminosidade no limite superior | (validador de planos de cultivo) | Unidade | Valores Limite (luminosidade = 25000 lux, limite superior exato) | Validador aceita o plano. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-53 | RN-53: luminosidade num valor interior | (validador de planos de cultivo) | Unidade | Valores Limite (luminosidade = 15000 lux, valor nominal) | Validador aceita o plano. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-54 | RN-54: plano pontual exige autorização do Responsável Técnico | (validador de planos de cultivo) | Unidade | Particionamento de Equivalência (autorização presente) | Validador aceita o plano pontual. | Nenhuma. Plano pontual com autorização preenchida. |
| TU-55 | RN-55: plano pontual sem autorização é rejeitado | (validador de planos de cultivo) | Unidade | Particionamento de Equivalência (autorização ausente / null) | Validador rejeita o plano pontual. | Nenhuma. Plano pontual sem campo de autorização. |
| TU-56 | RN-56: plano pontual com autorização vazia é rejeitado | (validador de planos de cultivo) | Unidade | Particionamento de Equivalência (autorização = "") | Validador rejeita o plano pontual. | Nenhuma. Plano pontual com autorização em branco. |

## Sprint 3 — Testes de Unidade dos Requisitos Restantes

| ID | Requisito / Regra | Endpoint | Nível | Técnica | Resultado Esperado | Pré-condições |
| --- | --- | --- | --- | --- | --- | --- |
| TU-57 | RN-57: aceita data no formato ISO (AAAA-MM-DD) | (validador de datas) | Unidade | Particionamento de Equivalência (formato válido: "2026-05-16") | Validador aceita a data. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-58 | RN-58: rejeita data no formato dia-mês-ano | (validador de datas) | Unidade | Particionamento de Equivalência (formato inválido: "16-05-2026") | Validador rejeita a data. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-59 | RN-59: rejeita data no formato mês-dia-ano | (validador de datas) | Unidade | Particionamento de Equivalência (formato inválido: "05-16-2026") | Validador rejeita a data. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-60 | RN-60: rejeita data com barras (dia/mês/ano) | (validador de datas) | Unidade | Particionamento de Equivalência (separador errado: "16/05/2026") | Validador rejeita a data. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-61 | RN-61: rejeita data com barras (ano/mês/dia) | (validador de datas) | Unidade | Particionamento de Equivalência (separador errado: "2026/05/16") | Validador rejeita a data. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-62 | RN-62: rejeita data sem separadores | (validador de datas) | Unidade | Particionamento de Equivalência (sem separadores: "20260516") | Validador rejeita a data. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-63 | RN-63: rejeita texto que não é data | (validador de datas) | Unidade | Particionamento de Equivalência (texto livre: "amanha") | Validador rejeita a data. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-64 | RN-64: rejeita data por extenso | (validador de datas) | Unidade | Particionamento de Equivalência (por extenso: "16 maio 2026") | Validador rejeita a data. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-65 | RN-65: rejeita mês inexistente | (validador de datas) | Unidade | Particionamento de Equivalência (mês 13: "2026-13-01") | Validador rejeita a data. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-66 | RN-66: rejeita dia inexistente | (validador de datas) | Unidade | Particionamento de Equivalência (30 de fevereiro: "2026-02-30") | Validador rejeita a data. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-67 | RN-67: lote ativo sem perdas conclui-se | (máquina de estados de lote) | Unidade | Particionamento de Equivalência (ativo, sem perdas, com data) | Lote transita para o estado "concluído". | Lote ativo, sem perdas registadas, com data de fim. |
| TU-68 | RN-68: lote ativo com perdas fica comprometido | (máquina de estados de lote) | Unidade | Particionamento de Equivalência (ativo, com perdas, com data) | Lote transita para o estado "comprometido". | Lote ativo, com perdas registadas, com data de fim. |
| TU-69 | RN-69: não fecha lote sem data de conclusão | (máquina de estados de lote) | Unidade | Particionamento de Equivalência (ativo, sem data de fim) | Rejeita a transição; equivale a 400 na API. | Lote ativo sem data de conclusão. |
| TU-70 | RN-70: lote já concluído não pode voltar a transitar | (máquina de estados de lote) | Unidade | Particionamento de Equivalência (estado terminal "concluído") | Rejeita a transição; equivale a 400 na API. | Lote no estado "concluído". |
| TU-71 | RN-71: lote comprometido não pode voltar a transitar | (máquina de estados de lote) | Unidade | Particionamento de Equivalência (estado terminal "comprometido") | Rejeita a transição; equivale a 400 na API. | Lote no estado "comprometido". |
| TU-72 | RN-72: estado de lote desconhecido é rejeitado | (máquina de estados de lote) | Unidade | Particionamento de Equivalência (estado inválido "suspenso") | Rejeita a transição; equivale a 400 na API. | Lote num estado fora dos previstos. |
| TU-73 | RN-73: produtividade total sem perdas | (calculadora de produtividade) | Unidade | Particionamento de Equivalência (colheita total, sem perdas) | Calcula 100% de produtividade. | Planeado 100, colhido 100, perdas 0. |
| TU-74 | RN-74: produtividade com perdas parciais | (calculadora de produtividade) | Unidade | Particionamento de Equivalência (colheita total, com perdas) | Calcula 80% de produtividade. | Planeado 100, colhido 100, perdas 20. |
| TU-75 | RN-75: produtividade com colheita parcial | (calculadora de produtividade) | Unidade | Particionamento de Equivalência (colheita abaixo do planeado) | Calcula 60% de produtividade. | Planeado 100, colhido 60, perdas 0. |
| TU-76 | RN-76: perdas não podem exceder a colheita | (calculadora de produtividade) | Unidade | Particionamento de Equivalência (perdas > colheita) | Rejeita o cálculo; equivale a 400 na API. | Planeado 100, colhido 50, perdas 60. |
| TU-77 | RN-77: quantidade planeada não pode ser zero | (calculadora de produtividade) | Unidade | Valores Limite (planeado = 0, divisão por zero) | Rejeita o cálculo; equivale a 400 na API. | Planeado 0. |
| TU-78 | RN-78: criação de lote com dados válidos | (validador de lotes) | Unidade | Particionamento de Equivalência (erva e quantidade válidas) | Validador aceita o lote. | Nenhuma. Erva id=1, quantidade planeada 100. |
| TU-79 | RN-79: lote exige indicação da erva | (validador de lotes) | Unidade | Particionamento de Equivalência (erva ausente) | Validador rejeita o lote; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-80 | RN-80: quantidade planeada não pode ser zero | (validador de lotes) | Unidade | Valores Limite (quantidade planeada = 0) | Validador rejeita o lote; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-81 | RN-81: quantidade planeada não pode ser negativa | (validador de lotes) | Unidade | Valores Limite (quantidade planeada = -10) | Validador rejeita o lote; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-82 | RN-82: aceita tarefa de rega | (validador de tarefas) | Unidade | Particionamento de Equivalência (tipo = "rega", classe válida) | Validador aceita a tarefa. | Nenhuma. Tarefa associada ao lote id=1. |
| TU-83 | RN-83: aceita tarefa de fertilização | (validador de tarefas) | Unidade | Particionamento de Equivalência (tipo = "fertilização", classe válida) | Validador aceita a tarefa. | Nenhuma. Tarefa associada ao lote id=1. |
| TU-84 | RN-84: aceita tarefa de colheita | (validador de tarefas) | Unidade | Particionamento de Equivalência (tipo = "colheita", classe válida) | Validador aceita a tarefa. | Nenhuma. Tarefa associada ao lote id=1. |
| TU-85 | RN-85: aceita tarefa de monitorização | (validador de tarefas) | Unidade | Particionamento de Equivalência (tipo = "monitorização", classe válida) | Validador aceita a tarefa. | Nenhuma. Tarefa associada ao lote id=1. |
| TU-86 | RN-86: rejeita tarefa de tipo desconhecido | (validador de tarefas) | Unidade | Particionamento de Equivalência (tipo = "outro", classe inválida) | Validador rejeita a tarefa; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-87 | RN-87: tarefa exige indicação do lote | (validador de tarefas) | Unidade | Particionamento de Equivalência (lote ausente) | Validador rejeita a tarefa; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-88 | RN-88: tarefa exige indicação do tipo | (validador de tarefas) | Unidade | Particionamento de Equivalência (tipo ausente) | Validador rejeita a tarefa; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-89 | RN-89: tarefa rejeita data em formato inválido | (validador de tarefas) | Unidade | Particionamento de Equivalência (data "16-05-2026", formato errado) | Validador rejeita a tarefa; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-90 | RN-90: temperatura abaixo do mínimo gera alerta | (registo de medições) | Unidade | Valores Limite (temperatura = 17 °C, abaixo de 18) | Regista a medição e gera um alerta. | Lote ativo (id=1) em memória, com limites padrão da estufa. |
| TU-91 | RN-91: temperatura no limite inferior não gera alerta | (registo de medições) | Unidade | Valores Limite (temperatura = 18 °C, limite inferior exato) | Regista a medição sem gerar alerta. | Lote ativo (id=1) em memória, com limites padrão da estufa. |
| TU-92 | RN-92: temperatura interior não gera alerta | (registo de medições) | Unidade | Valores Limite (temperatura = 23 °C, valor nominal) | Regista a medição sem gerar alerta. | Lote ativo (id=1) em memória, com limites padrão da estufa. |
| TU-93 | RN-93: temperatura no limite superior não gera alerta | (registo de medições) | Unidade | Valores Limite (temperatura = 28 °C, limite superior exato) | Regista a medição sem gerar alerta. | Lote ativo (id=1) em memória, com limites padrão da estufa. |
| TU-94 | RN-94: temperatura acima do máximo gera alerta | (registo de medições) | Unidade | Valores Limite (temperatura = 29 °C, acima de 28) | Regista a medição e gera um alerta. | Lote ativo (id=1) em memória, com limites padrão da estufa. |
| TU-95 | RN-95: humidade abaixo do mínimo gera alerta | (registo de medições) | Unidade | Valores Limite (humidade = 39 %, abaixo de 40) | Regista a medição e gera um alerta. | Lote ativo (id=1) em memória, com limites padrão da estufa. |
| TU-96 | RN-96: humidade no limite inferior não gera alerta | (registo de medições) | Unidade | Valores Limite (humidade = 40 %, limite inferior exato) | Regista a medição sem gerar alerta. | Lote ativo (id=1) em memória, com limites padrão da estufa. |
| TU-97 | RN-97: humidade interior não gera alerta | (registo de medições) | Unidade | Valores Limite (humidade = 60 %, valor nominal) | Regista a medição sem gerar alerta. | Lote ativo (id=1) em memória, com limites padrão da estufa. |
| TU-98 | RN-98: humidade no limite superior não gera alerta | (registo de medições) | Unidade | Valores Limite (humidade = 80 %, limite superior exato) | Regista a medição sem gerar alerta. | Lote ativo (id=1) em memória, com limites padrão da estufa. |
| TU-99 | RN-99: humidade acima do máximo gera alerta | (registo de medições) | Unidade | Valores Limite (humidade = 81 %, acima de 80) | Regista a medição e gera um alerta. | Lote ativo (id=1) em memória, com limites padrão da estufa. |
| TU-100 | RN-100: luminosidade abaixo do mínimo gera alerta informativo | (registo de medições) | Unidade | Valores Limite (luminosidade = 4999 lux, abaixo de 5000) | Regista a medição e gera um alerta de nível Informativo. | Lote ativo (id=1) em memória, com limites padrão da estufa. |
| TU-101 | RN-101: luminosidade no limite inferior não gera alerta | (registo de medições) | Unidade | Valores Limite (luminosidade = 5000 lux, limite inferior exato) | Regista a medição sem gerar alerta. | Lote ativo (id=1) em memória, com limites padrão da estufa. |
| TU-102 | RN-102: luminosidade interior não gera alerta | (registo de medições) | Unidade | Valores Limite (luminosidade = 15000 lux, valor nominal) | Regista a medição sem gerar alerta. | Lote ativo (id=1) em memória, com limites padrão da estufa. |
| TU-103 | RN-103: luminosidade no limite superior não gera alerta | (registo de medições) | Unidade | Valores Limite (luminosidade = 25000 lux, limite superior exato) | Regista a medição sem gerar alerta. | Lote ativo (id=1) em memória, com limites padrão da estufa. |
| TU-104 | RN-104: luminosidade acima do máximo gera alerta informativo | (registo de medições) | Unidade | Valores Limite (luminosidade = 25001 lux, acima de 25000) | Regista a medição e gera um alerta de nível Informativo. | Lote ativo (id=1) em memória, com limites padrão da estufa. |
| TU-105 | RN-105: sensor desligado nunca gera alerta | (registo de medições) | Unidade | Particionamento de Equivalência (sensor inoperacional) | Regista a medição sem gerar alerta, mesmo com leituras fora dos limites. | Lote ativo (id=1) em memória, com limites padrão da estufa. |
| TU-106 | RN-106: estado do sensor tem de ser booleano | (registo de medições) | Unidade | Particionamento de Equivalência (sensor = texto em vez de sim/não) | Rejeita a medição como entrada inválida; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-107 | RN-107: leituras normais não geram alerta | (classificador de alertas) | Unidade | Particionamento de Equivalência (tudo dentro dos limites) | Não classifica nenhum alerta. | Limites de referência: temp [18,28], humidade [40,80], luz [5000,25000]. |
| TU-108 | RN-108: temperatura alta gera Aviso | (classificador de alertas) | Unidade | Particionamento de Equivalência (só temperatura fora — 29 °C) | Classifica como "Aviso". | Limites de referência: temp [18,28], humidade [40,80], luz [5000,25000]. |
| TU-109 | RN-109: temperatura baixa gera Aviso | (classificador de alertas) | Unidade | Particionamento de Equivalência (só temperatura fora — 17 °C) | Classifica como "Aviso". | Limites de referência: temp [18,28], humidade [40,80], luz [5000,25000]. |
| TU-110 | RN-110: humidade alta gera Aviso | (classificador de alertas) | Unidade | Particionamento de Equivalência (só humidade fora — 85 %) | Classifica como "Aviso". | Limites de referência: temp [18,28], humidade [40,80], luz [5000,25000]. |
| TU-111 | RN-111: humidade baixa gera Aviso | (classificador de alertas) | Unidade | Particionamento de Equivalência (só humidade fora — 35 %) | Classifica como "Aviso". | Limites de referência: temp [18,28], humidade [40,80], luz [5000,25000]. |
| TU-112 | RN-112: temperatura e humidade fora geram Crítico | (classificador de alertas) | Unidade | Particionamento de Equivalência (duas leituras fora — 29 °C e 35 %) | Classifica como "Crítico". | Limites de referência: temp [18,28], humidade [40,80], luz [5000,25000]. |
| TU-113 | RN-113: só luminosidade fora gera Informativo | (classificador de alertas) | Unidade | Particionamento de Equivalência (só luminosidade fora — 26000 lux) | Classifica como "Informativo". | Limites de referência: temp [18,28], humidade [40,80], luz [5000,25000]. |
| TU-114 | RN-114: sensor desligado não gera alerta | (classificador de alertas) | Unidade | Particionamento de Equivalência (sensor inoperacional) | Não classifica alerta, mesmo com leituras fora dos limites. | Limites de referência: temp [18,28], humidade [40,80], luz [5000,25000]. |
| TU-115 | RN-115: resolver alerta sem justificação é permitido | (resolução de alertas) | Unidade | Particionamento de Equivalência (ação "resolvido", justificação opcional) | Alerta passa ao estado "resolvido". | Alerta no estado "pendente" em memória. |
| TU-116 | RN-116: resolver alerta com justificação é permitido | (resolução de alertas) | Unidade | Particionamento de Equivalência (ação "resolvido" com justificação) | Alerta passa ao estado "resolvido". | Alerta no estado "pendente" em memória. |
| TU-117 | RN-117: ignorar alerta com justificação válida é permitido | (resolução de alertas) | Unidade | Particionamento de Equivalência (ação "ignorado" com justificação válida) | Alerta passa ao estado "ignorado". | Alerta no estado "pendente" em memória. |
| TU-118 | RN-118: ignorar alerta exige justificação | (resolução de alertas) | Unidade | Particionamento de Equivalência (ação "ignorado" sem justificação) | Rejeita a operação; equivale a 422 na API. | Alerta no estado "pendente" em memória. |
| TU-119 | RN-119: ação de resolução desconhecida é rejeitada | (resolução de alertas) | Unidade | Particionamento de Equivalência (ação "cancelado", fora do permitido) | Rejeita a operação; equivale a 422 na API. | Alerta no estado "pendente" em memória. |
| TU-120 | RN-120: justificação para ignorar abaixo do mínimo | (resolução de alertas) | Unidade | Valores Limite (justificação = 9 caracteres, abaixo de 10) | Rejeita a operação; equivale a 422 na API. | Alerta no estado "pendente" em memória. |
| TU-121 | RN-121: justificação no limite inferior é aceite | (resolução de alertas) | Unidade | Valores Limite (justificação = 10 caracteres, limite inferior exato) | Alerta passa ao estado "ignorado". | Alerta no estado "pendente" em memória. |
| TU-122 | RN-122: justificação num tamanho interior é aceite | (resolução de alertas) | Unidade | Valores Limite (justificação = 250 caracteres, valor nominal) | Alerta passa ao estado "ignorado". | Alerta no estado "pendente" em memória. |
| TU-123 | RN-123: justificação no limite superior é aceite | (resolução de alertas) | Unidade | Valores Limite (justificação = 500 caracteres, limite superior exato) | Alerta passa ao estado "ignorado". | Alerta no estado "pendente" em memória. |
| TU-124 | RN-124: justificação acima do máximo é rejeitada | (resolução de alertas) | Unidade | Valores Limite (justificação = 501 caracteres, acima de 500) | Rejeita a operação; equivale a 422 na API. | Alerta no estado "pendente" em memória. |
| TU-125 | RN-125: resolver alerta inexistente é rejeitado | (resolução de alertas) | Unidade | Particionamento de Equivalência (id de alerta inexistente) | Rejeita a operação; equivale a 404 na API. | Registo de alertas vazio. |
| TU-126 | RN-126: alerta já tratado não pode ser alterado | (resolução de alertas) | Unidade | Particionamento de Equivalência (estado já não é "pendente") | Rejeita a operação; equivale a 422 na API. | Alerta já no estado "resolvido". |
| TU-127 | RN-127: modo automático com tudo ativo executa a ação | (motor de automação) | Unidade | Particionamento de Equivalência (automático, regra ativa, medição recente) | Decide "executada". | Modo automático, regra ativa, medição recente. |
| TU-128 | RN-128: modo manual com tudo ativo apenas sugere a ação | (motor de automação) | Unidade | Particionamento de Equivalência (manual, regra ativa, medição recente) | Decide "sugerida". | Modo manual, regra ativa, medição recente. |
| TU-129 | RN-129: regra inativa faz ignorar a ação | (motor de automação) | Unidade | Particionamento de Equivalência (regra inativa) | Decide "ignorada", qualquer que seja o modo. | Regra de automação inativa. |
| TU-130 | RN-130: medição não recente faz ignorar a ação | (motor de automação) | Unidade | Particionamento de Equivalência (medição desatualizada) | Decide "ignorada", qualquer que seja o modo. | Medição não recente. |
| TU-131 | RN-131: modo de automação desconhecido é rejeitado | (motor de automação) | Unidade | Particionamento de Equivalência (modo fora de {Manual, Automático}) | Rejeita a decisão; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-132 | RN-132: aceita perfil Técnico | (validador de utilizadores) | Unidade | Particionamento de Equivalência (perfil = "Técnico", classe válida) | Validador aceita o utilizador. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-133 | RN-133: aceita perfil Responsável Técnico | (validador de utilizadores) | Unidade | Particionamento de Equivalência (perfil = "Responsável Técnico", classe válida) | Validador aceita o utilizador. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-134 | RN-134: aceita perfil Administrador | (validador de utilizadores) | Unidade | Particionamento de Equivalência (perfil = "Administrador", classe válida) | Validador aceita o utilizador. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-135 | RN-135: rejeita perfil desconhecido | (validador de utilizadores) | Unidade | Particionamento de Equivalência (perfil = "Gestor", classe inválida) | Validador rejeita o utilizador; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-136 | RN-136: perfil é obrigatório | (validador de utilizadores) | Unidade | Particionamento de Equivalência (perfil ausente / null) | Validador rejeita o utilizador; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-137 | RN-137: aceita utilizador com todos os campos válidos | (validador de utilizadores) | Unidade | Particionamento de Equivalência (utilizador completo e válido) | Validador aceita o utilizador. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-138 | RN-138: nome de utilizador é obrigatório | (validador de utilizadores) | Unidade | Particionamento de Equivalência (username ausente) | Validador rejeita o utilizador; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-139 | RN-139: password é obrigatória | (validador de utilizadores) | Unidade | Particionamento de Equivalência (password ausente) | Validador rejeita o utilizador; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-140 | RN-140: perfil é obrigatório (campo em falta) | (validador de utilizadores) | Unidade | Particionamento de Equivalência (campo de perfil em falta) | Validador rejeita o utilizador; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-141 | RN-141: nome de utilizador não pode ser vazio | (validador de utilizadores) | Unidade | Particionamento de Equivalência (username = "") | Validador rejeita o utilizador; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-142 | RN-142: aceita exportação em CSV | (validador de formato de relatório) | Unidade | Particionamento de Equivalência (formato = "CSV", classe válida) | Validador aceita o formato. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-143 | RN-143: aceita exportação em Excel | (validador de formato de relatório) | Unidade | Particionamento de Equivalência (formato = "Excel", classe válida) | Validador aceita o formato. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-144 | RN-144: rejeita exportação em PDF | (validador de formato de relatório) | Unidade | Particionamento de Equivalência (formato = "PDF", classe inválida) | Validador rejeita o formato; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-145 | RN-145: rejeita exportação em JSON | (validador de formato de relatório) | Unidade | Particionamento de Equivalência (formato = "JSON", classe inválida) | Validador rejeita o formato; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-146 | RN-146: formato de exportação é obrigatório | (validador de formato de relatório) | Unidade | Particionamento de Equivalência (formato ausente / null) | Validador rejeita o formato; equivale a 400 na API. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-147 | RN-147: criação de lote é auditável | (registo de auditoria) | Unidade | Particionamento de Equivalência (operação de escrita) | Marca a operação como auditável. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-148 | RN-148: resolução de alerta é auditável | (registo de auditoria) | Unidade | Particionamento de Equivalência (operação de escrita) | Marca a operação como auditável. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-149 | RN-149: fecho de lote é auditável | (registo de auditoria) | Unidade | Particionamento de Equivalência (operação de escrita) | Marca a operação como auditável. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-150 | RN-150: consulta de lotes não é auditável | (registo de auditoria) | Unidade | Particionamento de Equivalência (operação de leitura) | Não marca a operação como auditável. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-151 | RN-151: consulta de ervas não é auditável | (registo de auditoria) | Unidade | Particionamento de Equivalência (operação de leitura) | Não marca a operação como auditável. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-164 | RN-164: duração do ciclo abaixo do mínimo | (validador de planos de cultivo) | Unidade | Valores Limite (duração = 0 dias, abaixo de 1) | Validador rejeita o plano. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-165 | RN-165: duração do ciclo no limite inferior | (validador de planos de cultivo) | Unidade | Valores Limite (duração = 1 dia, limite inferior exato) | Validador aceita o plano. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-166 | RN-166: duração do ciclo num valor interior | (validador de planos de cultivo) | Unidade | Valores Limite (duração = 90 dias, valor nominal) | Validador aceita o plano. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-167 | RN-167: duração do ciclo no limite superior | (validador de planos de cultivo) | Unidade | Valores Limite (duração = 365 dias, limite superior exato) | Validador aceita o plano. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |
| TU-168 | RN-168: duração do ciclo acima do máximo | (validador de planos de cultivo) | Unidade | Valores Limite (duração = 366 dias, acima de 365) | Validador rejeita o plano. | Nenhuma. Teste isolado sobre o serviço, sem BD nem rede. |

## Sprint 4 — Testes de Integração (FastAPI TestClient)

| ID | Requisito / Regra | Endpoint | Nível | Técnica | Resultado Esperado | Pré-condições |
| --- | --- | --- | --- | --- | --- | --- |
| TI-01 | RF-01: autenticação de utilizador | POST /auth/login | Integração | Particionamento de Equivalência (credenciais válidas) | 200 com token de acesso e token de renovação no corpo. | Aplicação em execução. Utilizadores predefinidos em memória. |
| TI-02 | RF-01: autenticação rejeita password errada | POST /auth/login | Integração | Particionamento de Equivalência (password errada) | 401 — autenticação recusada. | Aplicação em execução. Utilizadores predefinidos em memória. |
| TI-03 | RF-01: autenticação rejeita utilizador inexistente | POST /auth/login | Integração | Particionamento de Equivalência (username desconhecido) | 401 — autenticação recusada. | Aplicação em execução. Utilizadores predefinidos em memória. |
| TI-04 | RF-01: autenticação rejeita pedido sem dados | POST /auth/login | Integração | Particionamento de Equivalência (corpo vazio) | 400 ou 422 — pedido inválido. | Aplicação em execução (TestClient). Nenhum dado adicional necessário. |
| TI-05 | RF-02: renovação de sessão | POST /auth/refresh | Integração | Particionamento de Equivalência (token de renovação válido) | 200 com novo token de acesso. | Aplicação em execução. Token de renovação obtido por login prévio. |
| TI-06 | RF-02: renovação rejeita token malformado | POST /auth/refresh | Integração | Particionamento de Equivalência (token malformado) | 401 — renovação recusada. | Aplicação em execução (TestClient). Nenhum dado adicional necessário. |
| TI-07 | RF-01: método HTTP errado no login | GET /auth/login | Integração | Particionamento de Equivalência (GET onde só existe POST) | 405 — método não permitido. | Aplicação em execução (TestClient). Nenhum dado adicional necessário. |
| TI-08 | RF-03: consulta do catálogo exige autenticação | GET /herbs | Integração | Particionamento de Equivalência (sem token) | 401 — acesso não autorizado. | Aplicação em execução (TestClient). Nenhum dado adicional necessário. |
| TI-09 | RF-03: consulta do catálogo autenticada | GET /herbs | Integração | Particionamento de Equivalência (token válido) | 200 com a lista de ervas. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-10 | RF-04: importação de catálogo exige autenticação | POST /herbs/import | Integração | Particionamento de Equivalência (sem token) | 401 — acesso não autorizado. | Aplicação em execução (TestClient). Nenhum dado adicional necessário. |
| TI-11 | RF-04: importação restrita por perfil | POST /herbs/import | Integração | Particionamento de Equivalência (perfil Técnico, sem permissão) | 403 — perfil sem permissão. | Aplicação em execução. Técnico autenticado (JWT válido). |
| TI-12 | RF-04: importação de CSV válido pelo Administrador | POST /herbs/import | Integração | Particionamento de Equivalência (CSV válido, perfil Administrador) | 200; importa 2 ervas. | Aplicação em execução. Administrador autenticado. Catálogo vazio. |
| TI-13 | RF-04: importação rejeita ficheiro vazio | POST /herbs/import | Integração | Particionamento de Equivalência (CSV vazio) | 400 ou 422 — ficheiro inválido. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-14 | RF-05: criação de plano exige autenticação | POST /plans | Integração | Particionamento de Equivalência (sem token) | 401 — acesso não autorizado. | Aplicação em execução (TestClient). Nenhum dado adicional necessário. |
| TI-15 | RF-05: criação de plano regular | POST /plans | Integração | Particionamento de Equivalência (tipo regular, válido) | 201; plano criado com tipo "regular". | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-16 | RF-05: criação rejeita tipo de plano inválido | POST /plans | Integração | Particionamento de Equivalência (tipo desconhecido) | 400 — tipo de plano inválido. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-17 | RN-04: plano pontual exige autorização | POST /plans | Integração | Particionamento de Equivalência (pontual sem autorização) | 400 — autorização em falta. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-18 | RN-04: plano pontual com autorização é criado | POST /plans | Integração | Particionamento de Equivalência (pontual com autorização) | 201; plano criado com autorização preenchida. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-19 | RF-05: consulta de planos autenticada | GET /plans | Integração | Particionamento de Equivalência (token válido) | 200 com a lista de planos. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-20 | RF-05: método HTTP errado em planos | DELETE /plans | Integração | Particionamento de Equivalência (DELETE não suportado) | 405 — método não permitido. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-21 | RF-06: criação de lote exige autenticação | POST /batches | Integração | Particionamento de Equivalência (sem token) | 401 — acesso não autorizado. | Aplicação em execução (TestClient). Nenhum dado adicional necessário. |
| TI-22 | RF-06: criação de lote válido | POST /batches | Integração | Particionamento de Equivalência (dados válidos) | 201; lote criado no estado "ativo". | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-23 | RF-06: criação de lote sem erva | POST /batches | Integração | Particionamento de Equivalência (campo obrigatório em falta) | 422 — validação de esquema (campo erva em falta). | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-24 | RF-06: criação de lote com quantidade zero | POST /batches | Integração | Valores Limite (quantidade planeada = 0) | 400 — quantidade inválida. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-25 | RF-07: fecho de lote ativo | PATCH /batches/{id}/close | Integração | Particionamento de Equivalência (lote ativo) | 200; lote passa a "concluído". | Aplicação em execução. Administrador autenticado. Lote id=1 ativo. |
| TI-26 | RF-07: fecho de lote já concluído | PATCH /batches/{id}/close | Integração | Particionamento de Equivalência (estado terminal) | 400 — lote já fechado. | Aplicação em execução. Administrador autenticado. Lote id=1 fechado no próprio teste. |
| TI-27 | RF-07: fecho de lote inexistente | PATCH /batches/{id}/close | Integração | Particionamento de Equivalência (id inexistente) | 404 — lote não encontrado. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-28 | RF-06: consulta de lotes autenticada | GET /batches | Integração | Particionamento de Equivalência (token válido) | 200 com a lista de lotes. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-29 | RF-08: criação de tarefa exige autenticação | POST /tasks | Integração | Particionamento de Equivalência (sem token) | 401 — acesso não autorizado. | Aplicação em execução (TestClient). Nenhum dado adicional necessário. |
| TI-30 | RF-08: criação de tarefa válida | POST /tasks | Integração | Particionamento de Equivalência (tipo de tarefa válido) | 201; tarefa criada. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-31 | RF-08: criação rejeita tipo de tarefa inválido | POST /tasks | Integração | Particionamento de Equivalência (tipo desconhecido) | 400 — tipo de tarefa inválido. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-32 | RF-08: criação de tarefa sem lote | POST /tasks | Integração | Particionamento de Equivalência (campo obrigatório em falta) | 400 — lote em falta. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-33 | RF-08: consulta de tarefas autenticada | GET /tasks | Integração | Particionamento de Equivalência (token válido) | 200 com a lista de tarefas. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-34 | RF-08: método HTTP errado em tarefas | DELETE /tasks | Integração | Particionamento de Equivalência (DELETE não suportado) | 405 — método não permitido. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-35 | RF-09: registo de medição exige autenticação | POST /measurements | Integração | Particionamento de Equivalência (sem token) | 401 — acesso não autorizado. | Aplicação em execução (TestClient). Nenhum dado adicional necessário. |
| TI-36 | RF-09: medição dentro dos limites não gera alerta | POST /measurements | Integração | Particionamento de Equivalência (leituras normais) | 201; medição registada sem alerta. | Aplicação em execução. Administrador autenticado. Lote id=1 ativo. |
| TI-37 | RF-07/RN-02: medição fora dos limites gera alerta | POST /measurements | Integração | Valores Limite (temperatura acima do máximo) | 201; medição registada com alerta de nível "Aviso". | Aplicação em execução. Administrador autenticado. Lote id=1 ativo. |
| TI-38 | RF-09: medição com sensor desligado não gera alerta | POST /measurements | Integração | Particionamento de Equivalência (sensor inoperacional) | 201; medição registada sem alerta. | Aplicação em execução. Administrador autenticado. Lote id=1 ativo. |
| TI-39 | RF-09: consulta de medições autenticada | GET /measurements | Integração | Particionamento de Equivalência (token válido) | 200 com a lista de medições. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-40 | RF-09: medição com campos em falta | POST /measurements | Integração | Particionamento de Equivalência (campos obrigatórios em falta) | 400 ou 422 — pedido inválido. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-41 | RF-10: tratamento de alerta exige autenticação | PATCH /alerts/{id} | Integração | Particionamento de Equivalência (sem token) | 401 — acesso não autorizado. | Aplicação em execução. Alerta pendente em memória. |
| TI-42 | RF-10: consulta de alertas autenticada | GET /alerts | Integração | Particionamento de Equivalência (token válido) | 200 com a lista de alertas. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-43 | RF-10: resolver alerta sem justificação | PATCH /alerts/{id} | Integração | Particionamento de Equivalência (ação resolver, justificação opcional) | 200; alerta passa a "resolvido". | Aplicação em execução. Administrador autenticado. Alerta pendente. |
| TI-44 | RN-05: ignorar alerta com justificação válida | PATCH /alerts/{id} | Integração | Particionamento de Equivalência (ação ignorar, justificação válida) | 200; alerta passa a "ignorado". | Aplicação em execução. Administrador autenticado. Alerta pendente. |
| TI-45 | RN-05: ignorar alerta sem justificação | PATCH /alerts/{id} | Integração | Particionamento de Equivalência (ação ignorar, sem justificação) | 422 — justificação obrigatória. | Aplicação em execução. Administrador autenticado. Alerta pendente. |
| TI-46 | RN-05: justificação para ignorar abaixo do mínimo | PATCH /alerts/{id} | Integração | Valores Limite (justificação = 9 caracteres, abaixo de 10) | 422 — justificação demasiado curta. | Aplicação em execução. Administrador autenticado. Alerta pendente. |
| TI-47 | RN-05: justificação para ignorar acima do máximo | PATCH /alerts/{id} | Integração | Valores Limite (justificação = 501 caracteres, acima de 500) | 422 — justificação demasiado longa. | Aplicação em execução. Administrador autenticado. Alerta pendente. |
| TI-48 | RF-10: tratar alerta inexistente | PATCH /alerts/{id} | Integração | Particionamento de Equivalência (id inexistente) | 404 — alerta não encontrado. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-49 | RF-11: avaliação de automação exige autenticação | POST /automation/evaluate | Integração | Particionamento de Equivalência (sem token) | 401 — acesso não autorizado. | Aplicação em execução (TestClient). Nenhum dado adicional necessário. |
| TI-50 | RN-06: modo automático executa a ação | POST /automation/evaluate | Integração | Particionamento de Equivalência (automático, regra ativa, medição recente) | 200; decisão "executada". | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-51 | RN-06: modo manual sugere a ação | POST /automation/evaluate | Integração | Particionamento de Equivalência (manual, regra ativa, medição recente) | 200; decisão "sugerida". | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-52 | RN-06: regra inativa ignora a ação | POST /automation/evaluate | Integração | Particionamento de Equivalência (regra inativa) | 200; decisão "ignorada". | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-53 | RF-01/RN-01: criação de utilizador exige autenticação | POST /users | Integração | Particionamento de Equivalência (sem token) | 401 — acesso não autorizado. | Aplicação em execução (TestClient). Nenhum dado adicional necessário. |
| TI-54 | RF-01: criação de utilizador restrita a Administrador | POST /users | Integração | Particionamento de Equivalência (perfil Técnico, sem permissão) | 403 — perfil sem permissão. | Aplicação em execução. Técnico autenticado (JWT válido). |
| TI-55 | RF-01: Administrador cria utilizador | POST /users | Integração | Particionamento de Equivalência (perfil Administrador) | 201; utilizador criado com username e perfil. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-56 | RF-01: consulta de utilizadores autenticada | GET /users | Integração | Particionamento de Equivalência (token válido) | 200 com a lista de utilizadores. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-57 | RF-13: exportação de relatório exige autenticação | GET /reports | Integração | Particionamento de Equivalência (sem token) | 401 — acesso não autorizado. | Aplicação em execução (TestClient). Nenhum dado adicional necessário. |
| TI-58 | RF-13: exportação em CSV | GET /reports?format=CSV | Integração | Particionamento de Equivalência (formato CSV válido) | 200 — exportação aceite. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-59 | RF-13: exportação em Excel | GET /reports?format=Excel | Integração | Particionamento de Equivalência (formato Excel válido) | 200 — exportação aceite. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-60 | RF-13: exportação em formato não suportado | GET /reports?format=PDF | Integração | Particionamento de Equivalência (formato inválido) | 400 — formato não suportado. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-61 | RN-09: consulta de auditoria exige autenticação | GET /audit | Integração | Particionamento de Equivalência (sem token) | 401 — acesso não autorizado. | Aplicação em execução (TestClient). Nenhum dado adicional necessário. |
| TI-62 | RN-09: auditoria restrita por perfil | GET /audit | Integração | Particionamento de Equivalência (perfil Técnico, sem permissão) | 403 — perfil sem permissão. | Aplicação em execução. Técnico autenticado (JWT válido). |
| TI-63 | RN-09: Administrador consulta auditoria | GET /audit | Integração | Particionamento de Equivalência (perfil Administrador) | 200 com o registo de auditoria. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-64 | RN-09: método HTTP errado em auditoria | POST /audit | Integração | Particionamento de Equivalência (POST não suportado) | 405 — método não permitido. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-65 | RF-05: pedido com token malformado | POST /plans | Integração | Particionamento de Equivalência (token inválido no cabeçalho) | 401 — token inválido. | Aplicação em execução. Cabeçalho Authorization com token malformado. |
| TI-66 | RF-05: resposta de criação de plano tem todos os campos | POST /plans | Integração | Particionamento de Equivalência (verificação do esquema de resposta) | 201; corpo contém id, tipo, intervalos de temperatura, humidade, luminosidade e duração. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-67 | RF-06: resposta de criação de lote tem todos os campos | POST /batches | Integração | Particionamento de Equivalência (verificação do esquema de resposta) | 201; corpo contém id, erva, plano, estado, quantidades, perdas e produtividade. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-68 | RF-08: resposta de criação de tarefa tem todos os campos | POST /tasks | Integração | Particionamento de Equivalência (verificação do esquema de resposta) | 201; corpo contém id, lote, tipo de tarefa e data agendada. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-69 | RF-09: resposta de medição tem todos os campos | POST /measurements | Integração | Particionamento de Equivalência (verificação do esquema de resposta) | 201; corpo contém id, lote, leituras, estado do sensor e alerta. | Aplicação em execução. Administrador autenticado. Lote id=1 ativo. |
| TI-70 | RF-10: resposta de tratamento de alerta tem todos os campos | PATCH /alerts/{id} | Integração | Particionamento de Equivalência (verificação do esquema de resposta) | 200; corpo contém id, lote, nível, estado e justificação. | Aplicação em execução. Administrador autenticado. Alerta pendente. |
| TI-71 | RF-13: método HTTP errado em relatórios | POST /reports | Integração | Particionamento de Equivalência (POST não suportado) | 405 — método não permitido. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-72 | RF-10: método HTTP errado em alertas | DELETE /alerts/{id} | Integração | Particionamento de Equivalência (DELETE não suportado) | 405 — método não permitido. | Aplicação em execução. Administrador autenticado. Alerta pendente. |
| TI-73 | RF-09: método HTTP errado em medições | DELETE /measurements | Integração | Particionamento de Equivalência (DELETE não suportado) | 405 — método não permitido. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-74 | RF-05: criação de plano com tipo de dado errado | POST /plans | Integração | Particionamento de Equivalência (temperatura como texto) | 422 — validação de esquema. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-75 | RF-06: criação de lote com tipo de dado errado | POST /batches | Integração | Particionamento de Equivalência (erva como texto) | 422 — validação de esquema. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-76 | RN-06: avaliação de automação com modo inválido | POST /automation/evaluate | Integração | Particionamento de Equivalência (modo desconhecido) | 400 — modo inválido. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-77 | RF-01: criação de utilizador com perfil inválido | POST /users | Integração | Particionamento de Equivalência (perfil desconhecido) | 400 — perfil inválido. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-78 | RF-08: criação de tarefa com data inválida | POST /tasks | Integração | Particionamento de Equivalência (data em formato errado) | 400 — data inválida. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-79 | RF-10: consulta de alertas exige autenticação | GET /alerts | Integração | Particionamento de Equivalência (sem token) | 401 — acesso não autorizado. | Aplicação em execução (TestClient). Nenhum dado adicional necessário. |
| TI-80 | RF-11: método HTTP errado na automação | GET /automation/evaluate | Integração | Particionamento de Equivalência (GET não suportado) | 405 — método não permitido. | Aplicação em execução. Administrador autenticado (JWT válido). |
| TI-81 | RF-01: pedido com token expirado | GET /plans | Integração | Particionamento de Equivalência (token com validade no passado) | 401 — sessão expirada. | Aplicação em execução. Token gerado com expiração no passado. |
| TI-82 | RF-01: pedido com cabeçalho de autorização vazio | GET /plans | Integração | Particionamento de Equivalência (Authorization = "Bearer " sem token) | 401 — acesso não autorizado. | Aplicação em execução. Cabeçalho Authorization sem token. |
| TI-83 | RF-01: pedido com token de assinatura adulterada | GET /plans | Integração | Particionamento de Equivalência (assinatura alterada) | 401 — token inválido. | Aplicação em execução. Token válido com assinatura corrompida. |
| TI-84 | RF-02: renovação rejeita token de acesso | POST /auth/refresh | Integração | Particionamento de Equivalência (tipo de token errado) | 401 — tipo de token incorreto. | Aplicação em execução. Token de acesso (não de renovação) gerado. |
| TI-85 | RF-01: pedido autenticado com token válido | GET /plans | Integração | Particionamento de Equivalência (token de acesso válido e íntegro) | 200 com a lista de planos. | Aplicação em execução. Administrador autenticado (token íntegro, não expirado). |

## Sprint 5 — White-box: Cobertura de Condições / MC/DC (`validate_plan`)

| ID | Requisito / Regra | Endpoint | Nível | Técnica | Resultado Esperado | Pré-condições |
| --- | --- | --- | --- | --- | --- | --- |
| TU-152 | RN-152: plano regular completo é aceite (caso base) | (validador de planos de cultivo) | Unidade | Condições Múltiplas / MC/DC — caso de referência (todas as condições verdadeiras) | Validador aceita o plano. Serve de base aos pares MC/DC. | Plano regular com temperatura 23, humidade 60, luminosidade 15000. |
| TU-153 | RN-153: tipo de plano determina a aceitação | (validador de planos de cultivo) | Unidade | Condições Múltiplas / MC/DC — varia só o tipo (par com TU-152) | Validador rejeita o plano; prova que o tipo, por si só, muda o resultado. | Plano com tipo inválido, restantes parâmetros válidos. |
| TU-154 | RN-154: temperatura determina a aceitação | (validador de planos de cultivo) | Unidade | Condições Múltiplas / MC/DC — varia só a temperatura (par com TU-152) | Validador rejeita o plano; prova que a temperatura, por si só, muda o resultado. | Temperatura 17 (fora), restantes parâmetros válidos. |
| TU-155 | RN-155: humidade determina a aceitação | (validador de planos de cultivo) | Unidade | Condições Múltiplas / MC/DC — varia só a humidade (par com TU-152) | Validador rejeita o plano; prova que a humidade, por si só, muda o resultado. | Humidade 35 (fora), restantes parâmetros válidos. |
| TU-156 | RN-156: luminosidade determina a aceitação | (validador de planos de cultivo) | Unidade | Condições Múltiplas / MC/DC — varia só a luminosidade (par com TU-152) | Validador rejeita o plano; prova que a luminosidade, por si só, muda o resultado. | Luminosidade 4000 (fora), restantes parâmetros válidos. |
| TU-157 | RN-157: ser pontual determina a exigência de autorização | (validador de planos de cultivo) | Unidade | Condições Múltiplas / MC/DC — varia só o tipo pontual (par com TU-152) | Validador rejeita o plano pontual sem autorização; prova o efeito de ser pontual. | Plano pontual sem autorização, restantes parâmetros válidos. |
| TU-158 | RN-158: a autorização desbloqueia o plano pontual | (validador de planos de cultivo) | Unidade | Condições Múltiplas / MC/DC — varia só a autorização (par com TU-157) | Validador aceita o plano pontual; prova que a autorização, por si só, muda o resultado. | Plano pontual com autorização preenchida. |
| TU-159 | RN-159: pedido de plano malformado é rejeitado | (validador de planos de cultivo) | Unidade | White-box (cobertura de ramos — guarda de entrada) | Validador rejeita o pedido; equivale a 400 na API. | Nenhuma. Pedido sem corpo válido. |
| TU-160 | RN-160: temperatura tem de ser numérica | (validador de planos de cultivo) | Unidade | White-box (cobertura de ramos — verificação de tipo numérico) | Validador rejeita o plano; equivale a 400 na API. | Nenhuma. Temperatura como texto. |
| TU-161 | RN-161: temperatura máxima não pode ser menor que a mínima | (validador de planos de cultivo) | Unidade | White-box (cobertura de ramos — coerência mín/máx da temperatura) | Validador rejeita o plano; equivale a 400 na API. | Nenhuma. Temperatura mín 26, máx 22. |
| TU-162 | RN-162: humidade máxima não pode ser menor que a mínima | (validador de planos de cultivo) | Unidade | White-box (cobertura de ramos — coerência mín/máx da humidade) | Validador rejeita o plano; equivale a 400 na API. | Nenhuma. Humidade mín 70, máx 50. |
| TU-163 | RN-163: luminosidade máxima não pode ser menor que a mínima | (validador de planos de cultivo) | Unidade | White-box (cobertura de ramos — coerência mín/máx da luminosidade) | Validador rejeita o plano; equivale a 400 na API. | Nenhuma. Luminosidade mín 20000, máx 10000. |

## Sprint 6 — Duplos de Teste (Stubs e Mocks)

| ID | Requisito / Regra | Endpoint | Nível | Técnica | Resultado Esperado | Pré-condições |
| --- | --- | --- | --- | --- | --- | --- |
| TU-169 | RN-169: leitura de temperatura dentro dos limites não gera alerta | (monitoring_service + Stub do sensor) | Unidade | Stub (duplo de teste) — sensor devolve 23 °C | Serviço não gera alerta. | Stub configurado para devolver 23 °C. |
| TU-170 | RN-170: temperatura abaixo do mínimo gera alerta | (monitoring_service + Stub do sensor) | Unidade | Stub (duplo de teste) — sensor devolve 5 °C | Serviço gera alerta Crítico. | Stub configurado para devolver 5 °C. |
| TU-171 | RN-171: temperatura acima do máximo gera alerta | (monitoring_service + Stub do sensor) | Unidade | Stub (duplo de teste) — sensor devolve 31 °C | Serviço gera alerta Informativo. | Stub configurado para devolver 31 °C. |
| TU-172 | RN-172: sensor indisponível não rebenta a aplicação | (monitoring_service + Stub do sensor) | Unidade | Stub (duplo de teste) — sensor lança indisponibilidade | Serviço devolve estado "sensor indisponível" sem propagar exceção. | Stub configurado como indisponível. |
| TU-173 | RN-173: alerta Crítico envia notificação | (monitoring_service + Mock de notificações) | Unidade | Mock (duplo de teste) — verifica chamada e parâmetros | Notificação enviada 1×, com destinatário, assunto ([CRÍTICO], lote) e corpo corretos. | Stub devolve 40 °C (Crítico). Mock de notificações ativo. |
| TU-174 | RN-174: leitura dentro dos limites não envia notificação | (monitoring_service + Mock de notificações) | Unidade | Mock (duplo de teste) — verifica ausência de chamada | Nenhuma notificação enviada (mock sem chamadas). | Stub devolve 23 °C (sem alerta). Mock de notificações ativo. |
| TU-175 | RN-175: alerta Informativo não envia notificação | (monitoring_service + Mock de notificações) | Unidade | Mock (duplo de teste) — verifica ausência de chamada | Nenhuma notificação enviada (mock sem chamadas). | Stub devolve 31 °C (Informativo). Mock de notificações ativo. |
| TU-176 | RN-176: falha no envio de notificação não rebenta a aplicação | (monitoring_service + Mock de notificações) | Unidade | Mock (duplo de teste) — configurado para falhar | Alerta gerado; notificação não confirmada, sem exceção propagada. | Stub devolve 40 °C (Crítico). Mock configurado para falhar. |
| TU-177 | RN-177: desvio de 7 °C (35°C) classifica como Informativo e não notifica | (monitoring_service + Mock de notificações) | Unidade | Mock + Valores Limite (desvio = 7, fronteira inferior do Crítico) | Alerta Informativo; nenhuma notificação enviada. | Stub devolve 35 °C. Mock de notificações ativo. |
| TU-178 | RN-178: desvio de 8 °C (36°C) classifica como Crítico e notifica | (monitoring_service + Mock de notificações) | Unidade | Mock + Valores Limite (desvio = 8, imediatamente acima do limiar) | Alerta Crítico; notificação enviada 1×. | Stub devolve 36 °C. Mock de notificações ativo. |

## Testes de Sistema (nível obrigatório — secção 5.3)

| ID | Requisito / Regra | Endpoint | Nível | Técnica | Resultado Esperado | Pré-condições |
| --- | --- | --- | --- | --- | --- | --- |
| TS-01 | Fluxo E2E: ciclo completo de um lote | POST /herbs, /plans, /batches, /tasks, /measurements; PATCH /batches/{id}/close | Sistema | Combinação (PE + VL ao longo do fluxo) | Lote percorre ativo -> concluído; produtividade calculada (100%). | Aplicação em execução. Domínio vazio, apenas utilizadores predefinidos. Administrador autenticado. |
| TS-02 | Fluxo E2E: gestão de incidente | POST /batches, /measurements; GET /alerts; PATCH /alerts/{id} | Sistema | Valores Limite + Particionamento de Equivalência | Medição fora dos limites gera alerta; Responsável resolve-o com justificação. | Aplicação em execução. Lote ativo criado no fluxo. Administrador e Responsável autenticados. |
| TS-03 | Fluxo E2E: controlo de acesso à auditoria | GET /audit | Sistema | Particionamento de Equivalência (perfil = sem token / Técnico / Administrador) | 401 sem token; 403 para Técnico; 200 para Administrador. | Aplicação em execução. Utilizadores predefinidos (Técnico e Administrador). |

## Tabela Inversa Requisito -> Testes

| Requisito / Regra | Testes |
| --- | --- |
| RN-01: login com credenciais corretas | TU-01 |
| RN-02: login com password errada | TU-02 |
| RN-03: password não pode ser vazia | TU-03 |
| RN-04: password não pode ser nula | TU-04 |
| RN-05: password não pode ser só espaços | TU-05 |
| RN-06: password não pode exceder o tamanho máximo | TU-06 |
| RN-07: password não pode ter caracteres proibidos | TU-07 |
| RN-08: login com utilizador inexistente | TU-08 |
| RN-09: login com utilizador inexistente e password errada | TU-09 |
| RN-10: username não pode ser vazio | TU-10 |
| RN-11: username e password não podem ser ambos vazios | TU-11 |
| RN-12: username não pode ser nulo | TU-12 |
| RN-13: username e password não podem ser ambos nulos | TU-13 |
| RN-14: username não pode ser só espaços | TU-14 |
| RN-15: username não pode exceder o tamanho máximo | TU-15 |
| RN-16: username não pode ter caracteres proibidos | TU-16 |
| RN-17: emissão de token de acesso | TU-17 |
| RN-18: emissão de token de renovação | TU-18 |
| RN-19: não emite token sem utilizador | TU-19 |
| RN-20: não emite token de tipo desconhecido | TU-20 |
| RN-21: aceita token de acesso válido | TU-21 |
| RN-22: recusa token de acesso onde se espera renovação | TU-22 |
| RN-23: recusa token malformado | TU-23 |
| RN-24: recusa token vazio | TU-24 |
| RN-25: recusa token nulo | TU-25 |
| RN-26: recusa token com assinatura adulterada | TU-26 |
| RN-27: recusa token expirado | TU-27 |
| RN-28: renova a partir de token de renovação válido | TU-28 |
| RN-29: recusa renovação com token expirado | TU-29 |
| RN-30: recusa renovação com token malformado | TU-30 |
| RN-31: recusa renovação com token vazio | TU-31 |
| RN-32: recusa renovação com token nulo | TU-32 |
| RN-33: recusa renovação com token válido mas não registado | TU-33 |
| RN-34: importa ervas com campos opcionais vazios | TU-34 |
| RN-35: rejeita importação de ficheiro vazio | TU-35 |
| RN-36: reimportar as mesmas ervas cria duplicados | TU-36 |
| RN-37: importar ervas novas não duplica as existentes | TU-37 |
| RN-38: rejeita erva com nome de tipo errado | TU-38 |
| RN-39: temperatura abaixo do mínimo | TU-39 |
| RN-40: temperatura acima do máximo | TU-40 |
| RN-41: temperatura no limite inferior | TU-41 |
| RN-42: temperatura no limite superior | TU-42 |
| RN-43: temperatura num valor interior | TU-43 |
| RN-44: humidade abaixo do mínimo | TU-44 |
| RN-45: humidade acima do máximo | TU-45 |
| RN-46: humidade no limite inferior | TU-46 |
| RN-47: humidade no limite superior | TU-47 |
| RN-48: humidade num valor interior | TU-48 |
| RN-49: luminosidade abaixo do mínimo | TU-49 |
| RN-50: luminosidade acima do máximo | TU-50 |
| RN-51: luminosidade no limite inferior | TU-51 |
| RN-52: luminosidade no limite superior | TU-52 |
| RN-53: luminosidade num valor interior | TU-53 |
| RN-54: plano pontual exige autorização do Responsável Técnico | TU-54 |
| RN-55: plano pontual sem autorização é rejeitado | TU-55 |
| RN-56: plano pontual com autorização vazia é rejeitado | TU-56 |
| RN-57: aceita data no formato ISO (AAAA-MM-DD) | TU-57 |
| RN-58: rejeita data no formato dia-mês-ano | TU-58 |
| RN-59: rejeita data no formato mês-dia-ano | TU-59 |
| RN-60: rejeita data com barras (dia/mês/ano) | TU-60 |
| RN-61: rejeita data com barras (ano/mês/dia) | TU-61 |
| RN-62: rejeita data sem separadores | TU-62 |
| RN-63: rejeita texto que não é data | TU-63 |
| RN-64: rejeita data por extenso | TU-64 |
| RN-65: rejeita mês inexistente | TU-65 |
| RN-66: rejeita dia inexistente | TU-66 |
| RN-67: lote ativo sem perdas conclui-se | TU-67 |
| RN-68: lote ativo com perdas fica comprometido | TU-68 |
| RN-69: não fecha lote sem data de conclusão | TU-69 |
| RN-70: lote já concluído não pode voltar a transitar | TU-70 |
| RN-71: lote comprometido não pode voltar a transitar | TU-71 |
| RN-72: estado de lote desconhecido é rejeitado | TU-72 |
| RN-73: produtividade total sem perdas | TU-73 |
| RN-74: produtividade com perdas parciais | TU-74 |
| RN-75: produtividade com colheita parcial | TU-75 |
| RN-76: perdas não podem exceder a colheita | TU-76 |
| RN-77: quantidade planeada não pode ser zero | TU-77 |
| RN-78: criação de lote com dados válidos | TU-78 |
| RN-79: lote exige indicação da erva | TU-79 |
| RN-80: quantidade planeada não pode ser zero | TU-80 |
| RN-81: quantidade planeada não pode ser negativa | TU-81 |
| RN-82: aceita tarefa de rega | TU-82 |
| RN-83: aceita tarefa de fertilização | TU-83 |
| RN-84: aceita tarefa de colheita | TU-84 |
| RN-85: aceita tarefa de monitorização | TU-85 |
| RN-86: rejeita tarefa de tipo desconhecido | TU-86 |
| RN-87: tarefa exige indicação do lote | TU-87 |
| RN-88: tarefa exige indicação do tipo | TU-88 |
| RN-89: tarefa rejeita data em formato inválido | TU-89 |
| RN-90: temperatura abaixo do mínimo gera alerta | TU-90 |
| RN-91: temperatura no limite inferior não gera alerta | TU-91 |
| RN-92: temperatura interior não gera alerta | TU-92 |
| RN-93: temperatura no limite superior não gera alerta | TU-93 |
| RN-94: temperatura acima do máximo gera alerta | TU-94 |
| RN-95: humidade abaixo do mínimo gera alerta | TU-95 |
| RN-96: humidade no limite inferior não gera alerta | TU-96 |
| RN-97: humidade interior não gera alerta | TU-97 |
| RN-98: humidade no limite superior não gera alerta | TU-98 |
| RN-99: humidade acima do máximo gera alerta | TU-99 |
| RN-100: luminosidade abaixo do mínimo gera alerta informativo | TU-100 |
| RN-101: luminosidade no limite inferior não gera alerta | TU-101 |
| RN-102: luminosidade interior não gera alerta | TU-102 |
| RN-103: luminosidade no limite superior não gera alerta | TU-103 |
| RN-104: luminosidade acima do máximo gera alerta informativo | TU-104 |
| RN-105: sensor desligado nunca gera alerta | TU-105 |
| RN-106: estado do sensor tem de ser booleano | TU-106 |
| RN-107: leituras normais não geram alerta | TU-107 |
| RN-108: temperatura alta gera Aviso | TU-108 |
| RN-109: temperatura baixa gera Aviso | TU-109 |
| RN-110: humidade alta gera Aviso | TU-110 |
| RN-111: humidade baixa gera Aviso | TU-111 |
| RN-112: temperatura e humidade fora geram Crítico | TU-112 |
| RN-113: só luminosidade fora gera Informativo | TU-113 |
| RN-114: sensor desligado não gera alerta | TU-114 |
| RN-115: resolver alerta sem justificação é permitido | TU-115 |
| RN-116: resolver alerta com justificação é permitido | TU-116 |
| RN-117: ignorar alerta com justificação válida é permitido | TU-117 |
| RN-118: ignorar alerta exige justificação | TU-118 |
| RN-119: ação de resolução desconhecida é rejeitada | TU-119 |
| RN-120: justificação para ignorar abaixo do mínimo | TU-120 |
| RN-121: justificação no limite inferior é aceite | TU-121 |
| RN-122: justificação num tamanho interior é aceite | TU-122 |
| RN-123: justificação no limite superior é aceite | TU-123 |
| RN-124: justificação acima do máximo é rejeitada | TU-124 |
| RN-125: resolver alerta inexistente é rejeitado | TU-125 |
| RN-126: alerta já tratado não pode ser alterado | TU-126 |
| RN-127: modo automático com tudo ativo executa a ação | TU-127 |
| RN-128: modo manual com tudo ativo apenas sugere a ação | TU-128 |
| RN-129: regra inativa faz ignorar a ação | TU-129 |
| RN-130: medição não recente faz ignorar a ação | TU-130 |
| RN-131: modo de automação desconhecido é rejeitado | TU-131 |
| RN-132: aceita perfil Técnico | TU-132 |
| RN-133: aceita perfil Responsável Técnico | TU-133 |
| RN-134: aceita perfil Administrador | TU-134 |
| RN-135: rejeita perfil desconhecido | TU-135 |
| RN-136: perfil é obrigatório | TU-136 |
| RN-137: aceita utilizador com todos os campos válidos | TU-137 |
| RN-138: nome de utilizador é obrigatório | TU-138 |
| RN-139: password é obrigatória | TU-139 |
| RN-140: perfil é obrigatório (campo em falta) | TU-140 |
| RN-141: nome de utilizador não pode ser vazio | TU-141 |
| RN-142: aceita exportação em CSV | TU-142 |
| RN-143: aceita exportação em Excel | TU-143 |
| RN-144: rejeita exportação em PDF | TU-144 |
| RN-145: rejeita exportação em JSON | TU-145 |
| RN-146: formato de exportação é obrigatório | TU-146 |
| RN-147: criação de lote é auditável | TU-147 |
| RN-148: resolução de alerta é auditável | TU-148 |
| RN-149: fecho de lote é auditável | TU-149 |
| RN-150: consulta de lotes não é auditável | TU-150 |
| RN-151: consulta de ervas não é auditável | TU-151 |
| RN-152: plano regular completo é aceite (caso base) | TU-152 |
| RN-153: tipo de plano determina a aceitação | TU-153 |
| RN-154: temperatura determina a aceitação | TU-154 |
| RN-155: humidade determina a aceitação | TU-155 |
| RN-156: luminosidade determina a aceitação | TU-156 |
| RN-157: ser pontual determina a exigência de autorização | TU-157 |
| RN-158: a autorização desbloqueia o plano pontual | TU-158 |
| RN-159: pedido de plano malformado é rejeitado | TU-159 |
| RN-160: temperatura tem de ser numérica | TU-160 |
| RN-161: temperatura máxima não pode ser menor que a mínima | TU-161 |
| RN-162: humidade máxima não pode ser menor que a mínima | TU-162 |
| RN-163: luminosidade máxima não pode ser menor que a mínima | TU-163 |
| RN-164: duração do ciclo abaixo do mínimo | TU-164 |
| RN-165: duração do ciclo no limite inferior | TU-165 |
| RN-166: duração do ciclo num valor interior | TU-166 |
| RN-167: duração do ciclo no limite superior | TU-167 |
| RN-168: duração do ciclo acima do máximo | TU-168 |
| RN-169: leitura de temperatura dentro dos limites não gera alerta | TU-169 |
| RN-170: temperatura abaixo do mínimo gera alerta | TU-170 |
| RN-171: temperatura acima do máximo gera alerta | TU-171 |
| RN-172: sensor indisponível não rebenta a aplicação | TU-172 |
| RN-173: alerta Crítico envia notificação | TU-173 |
| RN-174: leitura dentro dos limites não envia notificação | TU-174 |
| RN-175: alerta Informativo não envia notificação | TU-175 |
| RN-176: falha no envio de notificação não rebenta a aplicação | TU-176 |
| RN-177: desvio de 7 °C (35°C) → Informativo, não notifica | TU-177 |
| RN-178: desvio de 8 °C (36°C) → Crítico, notifica | TU-178 |
| RF-01: autenticação de utilizador | TI-01 |
| RF-01: autenticação rejeita password errada | TI-02 |
| RF-01: autenticação rejeita utilizador inexistente | TI-03 |
| RF-01: autenticação rejeita pedido sem dados | TI-04 |
| RF-02: renovação de sessão | TI-05 |
| RF-02: renovação rejeita token malformado | TI-06 |
| RF-01: método HTTP errado no login | TI-07 |
| RF-03: consulta do catálogo exige autenticação | TI-08 |
| RF-03: consulta do catálogo autenticada | TI-09 |
| RF-04: importação de catálogo exige autenticação | TI-10 |
| RF-04: importação restrita por perfil | TI-11 |
| RF-04: importação de CSV válido pelo Administrador | TI-12 |
| RF-04: importação rejeita ficheiro vazio | TI-13 |
| RF-05: criação de plano exige autenticação | TI-14 |
| RF-05: criação de plano regular | TI-15 |
| RF-05: criação rejeita tipo de plano inválido | TI-16 |
| RN-04: plano pontual exige autorização | TI-17 |
| RN-04: plano pontual com autorização é criado | TI-18 |
| RF-05: consulta de planos autenticada | TI-19 |
| RF-05: método HTTP errado em planos | TI-20 |
| RF-06: criação de lote exige autenticação | TI-21 |
| RF-06: criação de lote válido | TI-22 |
| RF-06: criação de lote sem erva | TI-23 |
| RF-06: criação de lote com quantidade zero | TI-24 |
| RF-07: fecho de lote ativo | TI-25 |
| RF-07: fecho de lote já concluído | TI-26 |
| RF-07: fecho de lote inexistente | TI-27 |
| RF-06: consulta de lotes autenticada | TI-28 |
| RF-08: criação de tarefa exige autenticação | TI-29 |
| RF-08: criação de tarefa válida | TI-30 |
| RF-08: criação rejeita tipo de tarefa inválido | TI-31 |
| RF-08: criação de tarefa sem lote | TI-32 |
| RF-08: consulta de tarefas autenticada | TI-33 |
| RF-08: método HTTP errado em tarefas | TI-34 |
| RF-09: registo de medição exige autenticação | TI-35 |
| RF-09: medição dentro dos limites não gera alerta | TI-36 |
| RF-07/RN-02: medição fora dos limites gera alerta | TI-37 |
| RF-09: medição com sensor desligado não gera alerta | TI-38 |
| RF-09: consulta de medições autenticada | TI-39 |
| RF-09: medição com campos em falta | TI-40 |
| RF-10: tratamento de alerta exige autenticação | TI-41 |
| RF-10: consulta de alertas autenticada | TI-42 |
| RF-10: resolver alerta sem justificação | TI-43 |
| RN-05: ignorar alerta com justificação válida | TI-44 |
| RN-05: ignorar alerta sem justificação | TI-45 |
| RN-05: justificação para ignorar abaixo do mínimo | TI-46 |
| RN-05: justificação para ignorar acima do máximo | TI-47 |
| RF-10: tratar alerta inexistente | TI-48 |
| RF-11: avaliação de automação exige autenticação | TI-49 |
| RN-06: modo automático executa a ação | TI-50 |
| RN-06: modo manual sugere a ação | TI-51 |
| RN-06: regra inativa ignora a ação | TI-52 |
| RF-01/RN-01: criação de utilizador exige autenticação | TI-53 |
| RF-01: criação de utilizador restrita a Administrador | TI-54 |
| RF-01: Administrador cria utilizador | TI-55 |
| RF-01: consulta de utilizadores autenticada | TI-56 |
| RF-13: exportação de relatório exige autenticação | TI-57 |
| RF-13: exportação em CSV | TI-58 |
| RF-13: exportação em Excel | TI-59 |
| RF-13: exportação em formato não suportado | TI-60 |
| RN-09: consulta de auditoria exige autenticação | TI-61 |
| RN-09: auditoria restrita por perfil | TI-62 |
| RN-09: Administrador consulta auditoria | TI-63 |
| RN-09: método HTTP errado em auditoria | TI-64 |
| RF-05: pedido com token malformado | TI-65 |
| RF-05: resposta de criação de plano tem todos os campos | TI-66 |
| RF-06: resposta de criação de lote tem todos os campos | TI-67 |
| RF-08: resposta de criação de tarefa tem todos os campos | TI-68 |
| RF-09: resposta de medição tem todos os campos | TI-69 |
| RF-10: resposta de tratamento de alerta tem todos os campos | TI-70 |
| RF-13: método HTTP errado em relatórios | TI-71 |
| RF-10: método HTTP errado em alertas | TI-72 |
| RF-09: método HTTP errado em medições | TI-73 |
| RF-05: criação de plano com tipo de dado errado | TI-74 |
| RF-06: criação de lote com tipo de dado errado | TI-75 |
| RN-06: avaliação de automação com modo inválido | TI-76 |
| RF-01: criação de utilizador com perfil inválido | TI-77 |
| RF-08: criação de tarefa com data inválida | TI-78 |
| RF-10: consulta de alertas exige autenticação | TI-79 |
| RF-11: método HTTP errado na automação | TI-80 |
| RF-01: pedido com token expirado | TI-81 |
| RF-01: pedido com cabeçalho de autorização vazio | TI-82 |
| RF-01: pedido com token de assinatura adulterada | TI-83 |
| RF-02: renovação rejeita token de acesso | TI-84 |
| RF-01: pedido autenticado com token válido | TI-85 |
| Fluxo E2E: ciclo completo de um lote | TS-01 |
| Fluxo E2E: gestão de incidente | TS-02 |
| Fluxo E2E: controlo de acesso à auditoria | TS-03 |

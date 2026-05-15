# Matriz de Rastreabilidade

| ID | Requisito / Regra | Endpoint | Nível | Técnica | Resultado Esperado | Pré-condições |
| --- | --- | --- | --- | --- | --- | --- |
| TU-01 | RN-01: autenticação com username correto e password correta | POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Retorna utilizador sem password; 200 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-02 | RN-02: rejeita username correto com password errada | POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Retorna None; 401 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-03 | RN-03: rejeita username correto com password vazia | POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Lança AuthInputValidationError; 400 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-04 | RN-04: rejeita username correto com password null | POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Lança AuthInputValidationError; 400 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-05 | RN-05: rejeita username correto com password só com espaços | POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Lança AuthInputValidationError; 400 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-06 | RN-06: rejeita username correto com password demasiado longa | POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Lança AuthInputValidationError; 400 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-07 | RN-07: rejeita username correto com password com caracteres especiais | POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Lança AuthInputValidationError; 400 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-08 | RN-08: rejeita username inexistente com password correta | POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Retorna None; 401 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-09 | RN-09: rejeita username inexistente com password errada | POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Retorna None; 401 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-10 | RN-10: rejeita username vazio com password correta | POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Lança AuthInputValidationError; 400 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-11 | RN-11: rejeita username vazio com password vazia | POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Lança AuthInputValidationError; 400 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-12 | RN-12: rejeita username null com password correta | POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Lança AuthInputValidationError; 400 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-13 | RN-13: rejeita username null com password null | POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Lança AuthInputValidationError; 400 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-14 | RN-14: rejeita username só com espaços com password correta | POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Lança AuthInputValidationError; 400 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-15 | RN-15: rejeita username demasiado longo com password correta | POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Lança AuthInputValidationError; 400 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-16 | RN-16: rejeita username com caracteres especiais com password correta | POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Lança AuthInputValidationError; 400 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-17 | RN-17: emite access token para utilizador válido | POST /login; auth_service.generate_token | Unidade | Particionamento de Equivalência | Retorna JWT access com id, username, role, type e exp; 200 | Utilizador admin autenticado em memória. |
| TU-18 | RN-18: emite refresh token para utilizador válido | POST /login; auth_service.generate_token | Unidade | Particionamento de Equivalência | Retorna JWT refresh com id, username, role, type e exp; 200 | Utilizador admin autenticado em memória. |
| TU-19 | RN-19: rejeita emissão de token sem utilizador | POST /login; auth_service.generate_token | Unidade | Particionamento de Equivalência | Lança ValueError; 400 equivalente | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-20 | RN-20: rejeita emissão de token com tipo inválido | POST /login; auth_service.generate_token | Unidade | Particionamento de Equivalência | Lança ValueError; 400 equivalente | Utilizador admin autenticado em memória. |
| TU-21 | RN-21: descodifica access token válido | token validation; auth_service.decode_token | Unidade | Particionamento de Equivalência | Retorna payload correto; 200 | Access token admin gerado. |
| TU-22 | RN-22: rejeita access token quando é esperado refresh | POST /refresh; auth_service.decode_token | Unidade | Particionamento de Equivalência | Lança TokenValidationError; 401 | Access token admin gerado. |
| TU-23 | RN-23: rejeita token malformado | token validation; auth_service.decode_token | Unidade | Particionamento de Equivalência | Lança TokenValidationError; 401 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-24 | RN-24: rejeita token vazio | token validation; auth_service.decode_token | Unidade | Particionamento de Equivalência | Lança TokenValidationError; 401 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-25 | RN-25: rejeita token null | token validation; auth_service.decode_token | Unidade | Particionamento de Equivalência | Lança TokenValidationError; 401 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-26 | RN-26: rejeita token adulterado | token validation; auth_service.decode_token | Unidade | Particionamento de Equivalência | Lança TokenValidationError; 401 | Token válido gerado e assinatura alterada. |
| TU-27 | RN-27: rejeita token expirado | token validation; auth_service.decode_token | Unidade | Particionamento de Equivalência | Lança TokenValidationError; 401 | Token criado com expiração no passado. |
| TU-28 | RN-28: renova refresh token válido | POST /refresh; auth_service.refresh_token | Unidade | Particionamento de Equivalência | Retorna novo access_token e refresh_token; 200 | Refresh token admin válido e registado em memória. |
| TU-29 | RN-29: rejeita refresh token expirado | POST /refresh; auth_service.refresh_token | Unidade | Particionamento de Equivalência | Lança TokenValidationError; 401 | Refresh token criado com expiração no passado. |
| TU-30 | RN-30: rejeita refresh token malformado | POST /refresh; auth_service.refresh_token | Unidade | Particionamento de Equivalência | Lança TokenValidationError; 401 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-31 | RN-31: rejeita refresh token vazio | POST /refresh; auth_service.refresh_token | Unidade | Particionamento de Equivalência | Lança TokenValidationError; 401 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-32 | RN-32: rejeita refresh token null | POST /refresh; auth_service.refresh_token | Unidade | Particionamento de Equivalência | Lança TokenValidationError; 401 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-33 | RN-33: rejeita refresh token válido mas não registado | POST /refresh; auth_service.refresh_token | Unidade | Particionamento de Equivalência | Retorna None; 401 | Refresh token válido gerado e removido do store em memória. |
| TU-34 | RN-34: O catálogo está vazio e é possível importar registos com campos opcionais vazios | POST /herbs/import; herb_service.import_herbs_csv | Unidade | Particionamento de Equivalência | result['imported']==2; result['failed']==0; catálogo tem 2 entradas | Catálogo vazio (reset_herbs). Fixture CSV com name preenchido e family/description em branco. |
| TU-35 | RN-35: O catálogo está vazio e aparece um erro a informar que o ficheiro está vazio | POST /herbs/import; herb_service.import_herbs_csv | Unidade | Particionamento de Equivalência | Lança HerbValidationError com mensagem de ficheiro vazio; 400 | Catálogo vazio (reset_herbs). Conteúdo CSV = "". |
| TU-36 | RN-36: Importação do catálogo até ao momento com um novo registo e duplica os registos que já tinham sido importados | POST /herbs/import; herb_service.import_herbs_csv | Unidade | Particionamento de Equivalência | result['imported']==3; catálogo tem 5 entradas com Manjericão e Tomilho duplicados | Catálogo com 2 ervas (Manjericão, Tomilho) previamente importadas. CSV reimporta as 2 mesmas + Orégão nova. |
| TU-37 | RN-37: Importação do catálogo até ao momento com um novo registo e não duplica os que já existiam | POST /herbs/import; herb_service.import_herbs_csv | Unidade | Particionamento de Equivalência | result['imported']==2; catálogo tem 4 entradas; Manjericão e Tomilho com count==1 | Catálogo com 2 ervas (Manjericão, Tomilho). CSV importa apenas Orégão e Menta (nomes distintos dos existentes). |
| TU-38 | RN-38: Os tipos de inputs serem diferentes do esperado: name inteiro em vez de string | POST /herbs; herb_service.validate_herb | Unidade | Particionamento de Equivalência | Lança HerbValidationError; 400 | Nenhuma. Teste isolado com payload {"name": 123}. |
| TU-39 | RN-39: A criação do plano de cultivo tem um valor de temperatura com 17º | POST /plans; plan_service.validate_plan | Unidade | Análise de Valores Limite (temp=17, abaixo do mínimo 18) | Lança PlanValidationError; 400 | Nenhuma. Teste isolado. |
| TU-40 | RN-40: A criação do plano de cultivo tem um valor de temperatura com 29º | POST /plans; plan_service.validate_plan | Unidade | Análise de Valores Limite (temp=29, acima do máximo 28) | Lança PlanValidationError; 400 | Nenhuma. Teste isolado. |
| TU-41 | RN-41: A criação do plano de cultivo tem um valor de temperatura com 18º | POST /plans; plan_service.validate_plan | Unidade | Análise de Valores Limite (temp=18, limite inferior exacto) | validate_plan não lança; 201 | Nenhuma. Teste isolado. |
| TU-42 | RN-42: A criação do plano de cultivo tem um valor de temperatura com 28º | POST /plans; plan_service.validate_plan | Unidade | Análise de Valores Limite (temp=28, limite superior exacto) | validate_plan não lança; 201 | Nenhuma. Teste isolado. |
| TU-43 | RN-43: A criação do plano de cultivo tem um valor de temperatura com 23º | POST /plans; plan_service.validate_plan | Unidade | Análise de Valores Limite (temp=23, valor nominal interior) | validate_plan não lança; 201 | Nenhuma. Teste isolado. |
| TU-44 | RN-44: A criação do plano de cultivo tem um valor de humidade relativa com 39% | POST /plans; plan_service.validate_plan | Unidade | Análise de Valores Limite (hum=39, abaixo do mínimo 40) | Lança PlanValidationError; 400 | Nenhuma. Teste isolado. |
| TU-45 | RN-45: A criação do plano de cultivo tem um valor de humidade relativa com 81% | POST /plans; plan_service.validate_plan | Unidade | Análise de Valores Limite (hum=81, acima do máximo 80) | Lança PlanValidationError; 400 | Nenhuma. Teste isolado. |
| TU-46 | RN-46: A criação do plano de cultivo tem um valor de humidade relativa com 40% | POST /plans; plan_service.validate_plan | Unidade | Análise de Valores Limite (hum=40, limite inferior exacto) | validate_plan não lança; 201 | Nenhuma. Teste isolado. |
| TU-47 | RN-47: A criação do plano de cultivo tem um valor de humidade relativa com 80% | POST /plans; plan_service.validate_plan | Unidade | Análise de Valores Limite (hum=80, limite superior exacto) | validate_plan não lança; 201 | Nenhuma. Teste isolado. |
| TU-48 | RN-48: A criação do plano de cultivo tem um valor de humidade relativa com 64% | POST /plans; plan_service.validate_plan | Unidade | Análise de Valores Limite (hum=64, valor nominal interior) | validate_plan não lança; 201 | Nenhuma. Teste isolado. |
| TU-49 | RN-49: A criação do plano de cultivo tem um valor de luminosidade(lux) de 4999 | POST /plans; plan_service.validate_plan | Unidade | Análise de Valores Limite (lux=4999, abaixo do mínimo 5000) | Lança PlanValidationError; 400 | Nenhuma. Teste isolado. |
| TU-50 | RN-50: A criação do plano de cultivo tem um valor de luminosidade(lux) de 25001 | POST /plans; plan_service.validate_plan | Unidade | Análise de Valores Limite (lux=25001, acima do máximo 25000) | Lança PlanValidationError; 400 | Nenhuma. Teste isolado. |
| TU-51 | RN-51: A criação do plano de cultivo tem um valor de luminosidade(lux) de 5000 | POST /plans; plan_service.validate_plan | Unidade | Análise de Valores Limite (lux=5000, limite inferior exacto) | validate_plan não lança; 201 | Nenhuma. Teste isolado. |
| TU-52 | RN-52: A criação do plano de cultivo tem um valor de luminosidade(lux) de 25000 | POST /plans; plan_service.validate_plan | Unidade | Análise de Valores Limite (lux=25000, limite superior exacto) | validate_plan não lança; 201 | Nenhuma. Teste isolado. |
| TU-53 | RN-53: A criação do plano de cultivo tem um valor de luminosidade(lux) de 15000 | POST /plans; plan_service.validate_plan | Unidade | Análise de Valores Limite (lux=15000, valor nominal interior) | validate_plan não lança; 201 | Nenhuma. Teste isolado. |
| TU-54 | RN-54: Plano pontual criado com autorização do Responsável Técnico presente | POST /plans; plan_service.validate_plan | Unidade | Particionamento de Equivalência (authorized_by válido) | validate_plan não lança; 201 | Nenhuma. Teste isolado com payload {"type":"pontual","authorized_by":"responsavel"}. |
| TU-55 | RN-55: Plano pontual rejeitado quando authorized_by está ausente (null) | POST /plans; plan_service.validate_plan | Unidade | Particionamento de Equivalência (authorized_by null) | Lança PlanValidationError; 400 | Nenhuma. Teste isolado com payload {"type":"pontual","authorized_by":null}. |
| TU-56 | RN-56: Plano pontual rejeitado quando authorized_by está vazio ("") | POST /plans; plan_service.validate_plan | Unidade | Particionamento de Equivalência (authorized_by vazio) | Lança PlanValidationError; 400 | Nenhuma. Teste isolado com payload {"type":"pontual","authorized_by":""}. |
| TU-57 | RN-57: C1=F C2=F C3=F — sensor off, leituras normais | alert_service.classify_alert | Unidade | Condições Múltiplas / MC/DC (linha 1 da tabela de verdade) | Retorna None | Limites: temp_max=28, humidity_min=40. temp=23, hum=60, sensor_ok=False. |
| TU-58 | RN-58: C1=F C2=F C3=T — sensor on, ambas leituras normais | alert_service.classify_alert | Unidade | Condições Múltiplas / MC/DC (linha 2 — par MC/DC de C1 e C2) | Retorna None | Limites: temp_max=28, humidity_min=40. temp=23, hum=60, sensor_ok=True. |
| TU-59 | RN-59: C1=F C2=T C3=F — humidade baixa mas sensor off | alert_service.classify_alert | Unidade | Condições Múltiplas / MC/DC (linha 3 — par MC/DC de C3) | Retorna None | Limites: temp_max=28, humidity_min=40. temp=23, hum=35, sensor_ok=False. |
| TU-60 | RN-60: C1=F C2=T C3=T — humidade baixa, sensor on → Aviso | alert_service.classify_alert | Unidade | Condições Múltiplas / MC/DC (linha 4 — par MC/DC de C2 e C3) | Retorna "Aviso" | Limites: temp_max=28, humidity_min=40. temp=23, hum=35, sensor_ok=True. |
| TU-61 | RN-61: C1=T C2=F C3=F — temperatura alta mas sensor off | alert_service.classify_alert | Unidade | Condições Múltiplas / MC/DC (linha 5) | Retorna None | Limites: temp_max=28, humidity_min=40. temp=30, hum=60, sensor_ok=False. |
| TU-62 | RN-62: C1=T C2=F C3=T — temperatura alta, sensor on → Aviso | alert_service.classify_alert | Unidade | Condições Múltiplas / MC/DC (linha 6 — par MC/DC de C1) | Retorna "Aviso" | Limites: temp_max=28, humidity_min=40. temp=30, hum=60, sensor_ok=True. |
| TU-63 | RN-63: C1=T C2=T C3=F — ambos violados mas sensor off | alert_service.classify_alert | Unidade | Condições Múltiplas / MC/DC (linha 7 — par MC/DC de C3) | Retorna None | Limites: temp_max=28, humidity_min=40. temp=30, hum=35, sensor_ok=False. |
| TU-64 | RN-64: C1=T C2=T C3=T — ambas leituras violadas, sensor on → Crítico | alert_service.classify_alert | Unidade | Condições Múltiplas / MC/DC (linha 8 — resultado Crítico) | Retorna "Crítico" | Limites: temp_max=28, humidity_min=40. temp=30, hum=35, sensor_ok=True. |
| TU-65 | RN-65: lote ativo sem perdas com data definida → concluído | batch_service.transition_batch_state | Unidade | Particionamento de Equivalência (C1=T C2=F C3=T) | Retorna "concluído" | current_state="ativo", has_losses=False, end_date_set=True. |
| TU-66 | RN-66: lote ativo com perdas e data definida → comprometido | batch_service.transition_batch_state | Unidade | Particionamento de Equivalência (C1=T C2=T C3=T) | Retorna "comprometido" | current_state="ativo", has_losses=True, end_date_set=True. |
| TU-67 | RN-67: lote ativo sem data de conclusão → erro | batch_service.transition_batch_state | Unidade | Particionamento de Equivalência (C3=F) | Lança BatchStateError; 400 | current_state="ativo", end_date_set=False. |
| TU-68 | RN-68: lote já concluído não pode transicionar | batch_service.transition_batch_state | Unidade | Particionamento de Equivalência (estado terminal) | Lança BatchStateError; 400 | current_state="concluído". |
| TU-69 | RN-69: lote comprometido não pode transicionar | batch_service.transition_batch_state | Unidade | Particionamento de Equivalência (estado terminal) | Lança BatchStateError; 400 | current_state="comprometido". |
| TU-70 | RN-70: estado inválido ("suspenso") → erro imediato | batch_service.transition_batch_state | Unidade | Particionamento de Equivalência (estado desconhecido) | Lança BatchStateError; 400 | current_state="suspenso". |
| TU-71 | RN-71: sem perdas, colheita total → produtividade 100% | batch_service.calculate_productivity | Unidade | Particionamento de Equivalência (classe válida sem perdas) | Retorna 100.0 | planned_qty=100, actual_qty=100, losses=0. |
| TU-72 | RN-72: com perdas parciais → produtividade 80% | batch_service.calculate_productivity | Unidade | Particionamento de Equivalência (classe válida com perdas) | Retorna 80.0 | planned_qty=100, actual_qty=100, losses=20. |
| TU-73 | RN-73: colheita parcial sem perdas → produtividade 60% | batch_service.calculate_productivity | Unidade | Particionamento de Equivalência (colheita incompleta) | Retorna 60.0 | planned_qty=100, actual_qty=60, losses=0. |
| TU-74 | RN-74: perdas superiores à colheita → erro | batch_service.calculate_productivity | Unidade | Particionamento de Equivalência (losses > actual_qty) | Lança BatchCalculationError; 400 | planned_qty=100, actual_qty=50, losses=60. |
| TU-75 | RN-75: planned_qty = 0 → divisão por zero → erro | batch_service.calculate_productivity | Unidade | Valores Limite (planned_qty=0) | Lança BatchCalculationError; 400 | planned_qty=0. |
| TU-76 | RN-76: modo Automático + regra ativa + medição recente → executada | automation_service.decide_automation | Unidade | Condições Múltiplas / MC/DC (C1=T C2=T C3=T) | Retorna "executada" | mode="Automático", rule_active=True, measurement_recent=True. |
| TU-77 | RN-77: modo Manual + regra ativa + medição recente → sugerida | automation_service.decide_automation | Unidade | Condições Múltiplas / MC/DC (C1=F C2=T C3=T) | Retorna "sugerida" | mode="Manual", rule_active=True, measurement_recent=True. |
| TU-78 | RN-78: regra inativa → ignorada independentemente do modo | automation_service.decide_automation | Unidade | Condições Múltiplas / MC/DC (C2=F) | Retorna "ignorada" | mode="Automático", rule_active=False, measurement_recent=True. |
| TU-79 | RN-79: medição não recente → ignorada independentemente do modo | automation_service.decide_automation | Unidade | Condições Múltiplas / MC/DC (C3=F) | Retorna "ignorada" | mode="Manual", rule_active=True, measurement_recent=False. |

## Tabela Inversa Requisito -> Testes

| Requisito / Regra | Testes |
| --- | --- |
| RN-01: autenticação com username correto e password correta | TU-01 |
| RN-02: rejeita username correto com password errada | TU-02 |
| RN-03: rejeita username correto com password vazia | TU-03 |
| RN-04: rejeita username correto com password null | TU-04 |
| RN-05: rejeita username correto com password só com espaços | TU-05 |
| RN-06: rejeita username correto com password demasiado longa | TU-06 |
| RN-07: rejeita username correto com password com caracteres especiais | TU-07 |
| RN-08: rejeita username inexistente com password correta | TU-08 |
| RN-09: rejeita username inexistente com password errada | TU-09 |
| RN-10: rejeita username vazio com password correta | TU-10 |
| RN-11: rejeita username vazio com password vazia | TU-11 |
| RN-12: rejeita username null com password correta | TU-12 |
| RN-13: rejeita username null com password null | TU-13 |
| RN-14: rejeita username só com espaços com password correta | TU-14 |
| RN-15: rejeita username demasiado longo com password correta | TU-15 |
| RN-16: rejeita username com caracteres especiais com password correta | TU-16 |
| RN-17: emite access token para utilizador válido | TU-17 |
| RN-18: emite refresh token para utilizador válido | TU-18 |
| RN-19: rejeita emissão de token sem utilizador | TU-19 |
| RN-20: rejeita emissão de token com tipo inválido | TU-20 |
| RN-21: descodifica access token válido | TU-21 |
| RN-22: rejeita access token quando é esperado refresh | TU-22 |
| RN-23: rejeita token malformado | TU-23 |
| RN-24: rejeita token vazio | TU-24 |
| RN-25: rejeita token null | TU-25 |
| RN-26: rejeita token adulterado | TU-26 |
| RN-27: rejeita token expirado | TU-27 |
| RN-28: renova refresh token válido | TU-28 |
| RN-29: rejeita refresh token expirado | TU-29 |
| RN-30: rejeita refresh token malformado | TU-30 |
| RN-31: rejeita refresh token vazio | TU-31 |
| RN-32: rejeita refresh token null | TU-32 |
| RN-33: rejeita refresh token válido mas não registado | TU-33 |
| RN-34: importação CSV com catálogo vazio e campos opcionais em branco | TU-34 |
| RN-35: importação CSV com ficheiro vazio gera erro | TU-35 |
| RN-36: re-importação do mesmo catálogo cria duplicados | TU-36 |
| RN-37: importação de ervas novas não duplica as existentes | TU-37 |
| RN-38: tipo de input errado (name inteiro) gera erro | TU-38 |
| RN-39: temperatura 17°C rejeitada (abaixo do mínimo) | TU-39 |
| RN-40: temperatura 29°C rejeitada (acima do máximo) | TU-40 |
| RN-41: temperatura 18°C aceite (limite inferior) | TU-41 |
| RN-42: temperatura 28°C aceite (limite superior) | TU-42 |
| RN-43: temperatura 23°C aceite (valor nominal) | TU-43 |
| RN-44: humidade 39% rejeitada (abaixo do mínimo) | TU-44 |
| RN-45: humidade 81% rejeitada (acima do máximo) | TU-45 |
| RN-46: humidade 40% aceite (limite inferior) | TU-46 |
| RN-47: humidade 80% aceite (limite superior) | TU-47 |
| RN-48: humidade 64% aceite (valor nominal) | TU-48 |
| RN-49: luminosidade 4999 lux rejeitada (abaixo do mínimo) | TU-49 |
| RN-50: luminosidade 25001 lux rejeitada (acima do máximo) | TU-50 |
| RN-51: luminosidade 5000 lux aceite (limite inferior) | TU-51 |
| RN-52: luminosidade 25000 lux aceite (limite superior) | TU-52 |
| RN-53: luminosidade 15000 lux aceite (valor nominal) | TU-53 |
| RN-54: plano pontual com authorized_by válido é aceite | TU-54 |
| RN-55: plano pontual sem authorized_by (null) é rejeitado | TU-55 |
| RN-56: plano pontual com authorized_by vazio é rejeitado | TU-56 |
| RN-57: classify_alert C1=F C2=F C3=F → None | TU-57 |
| RN-58: classify_alert C1=F C2=F C3=T → None | TU-58 |
| RN-59: classify_alert C1=F C2=T C3=F → None | TU-59 |
| RN-60: classify_alert C1=F C2=T C3=T → "Aviso" | TU-60 |
| RN-61: classify_alert C1=T C2=F C3=F → None | TU-61 |
| RN-62: classify_alert C1=T C2=F C3=T → "Aviso" | TU-62 |
| RN-63: classify_alert C1=T C2=T C3=F → None | TU-63 |
| RN-64: classify_alert C1=T C2=T C3=T → "Crítico" | TU-64 |
| RN-65: lote ativo sem perdas + data definida → "concluído" | TU-65 |
| RN-66: lote ativo com perdas + data definida → "comprometido" | TU-66 |
| RN-67: lote ativo sem data de conclusão → BatchStateError | TU-67 |
| RN-68: lote concluído não pode transicionar → BatchStateError | TU-68 |
| RN-69: lote comprometido não pode transicionar → BatchStateError | TU-69 |
| RN-70: estado inválido → BatchStateError | TU-70 |
| RN-71: sem perdas, colheita total → produtividade 100% | TU-71 |
| RN-72: com perdas parciais → produtividade 80% | TU-72 |
| RN-73: colheita parcial sem perdas → produtividade 60% | TU-73 |
| RN-74: losses > actual_qty → BatchCalculationError | TU-74 |
| RN-75: planned_qty = 0 → BatchCalculationError | TU-75 |
| RN-76: Automático + regra ativa + medição recente → "executada" | TU-76 |
| RN-77: Manual + regra ativa + medição recente → "sugerida" | TU-77 |
| RN-78: regra inativa → "ignorada" | TU-78 |
| RN-79: medição não recente → "ignorada" | TU-79 |

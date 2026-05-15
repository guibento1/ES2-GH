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
| TU-57 | RN-57: C1=F C2=F C3=F — sensor off, leituras normais | POST /measurements; alert_service.classify_alert | Unidade | Condições Múltiplas / MC/DC (linha 1 da tabela de verdade) | Retorna None | Limites: temp_max=28, humidity_min=40. temp=23, hum=60, sensor_ok=False. |
| TU-58 | RN-58: C1=F C2=F C3=T — sensor on, ambas leituras normais | POST /measurements; alert_service.classify_alert | Unidade | Condições Múltiplas / MC/DC (linha 2 — par MC/DC de C1 e C2) | Retorna None | Limites: temp_max=28, humidity_min=40. temp=23, hum=60, sensor_ok=True. |
| TU-59 | RN-59: C1=F C2=T C3=F — humidade baixa mas sensor off | POST /measurements; alert_service.classify_alert | Unidade | Condições Múltiplas / MC/DC (linha 3 — par MC/DC de C3) | Retorna None | Limites: temp_max=28, humidity_min=40. temp=23, hum=35, sensor_ok=False. |
| TU-60 | RN-60: C1=F C2=T C3=T — humidade baixa, sensor on → Aviso | POST /measurements; alert_service.classify_alert | Unidade | Condições Múltiplas / MC/DC (linha 4 — par MC/DC de C2 e C3) | Retorna "Aviso" | Limites: temp_max=28, humidity_min=40. temp=23, hum=35, sensor_ok=True. |
| TU-61 | RN-61: C1=T C2=F C3=F — temperatura alta mas sensor off | POST /measurements; alert_service.classify_alert | Unidade | Condições Múltiplas / MC/DC (linha 5) | Retorna None | Limites: temp_max=28, humidity_min=40. temp=30, hum=60, sensor_ok=False. |
| TU-62 | RN-62: C1=T C2=F C3=T — temperatura alta, sensor on → Aviso | POST /measurements; alert_service.classify_alert | Unidade | Condições Múltiplas / MC/DC (linha 6 — par MC/DC de C1) | Retorna "Aviso" | Limites: temp_max=28, humidity_min=40. temp=30, hum=60, sensor_ok=True. |
| TU-63 | RN-63: C1=T C2=T C3=F — ambos violados mas sensor off | POST /measurements; alert_service.classify_alert | Unidade | Condições Múltiplas / MC/DC (linha 7 — par MC/DC de C3) | Retorna None | Limites: temp_max=28, humidity_min=40. temp=30, hum=35, sensor_ok=False. |
| TU-64 | RN-64: C1=T C2=T C3=T — ambas leituras violadas, sensor on → Crítico | POST /measurements; alert_service.classify_alert | Unidade | Condições Múltiplas / MC/DC (linha 8 — resultado Crítico) | Retorna "Crítico" | Limites: temp_max=28, humidity_min=40. temp=30, hum=35, sensor_ok=True. |
| TU-65 | RN-65: lote ativo sem perdas com data definida → concluído | PATCH /batches/{id}/close; batch_service.transition_batch_state | Unidade | Particionamento de Equivalência (C1=T C2=F C3=T) | Retorna "concluído" | current_state="ativo", has_losses=False, end_date_set=True. |
| TU-66 | RN-66: lote ativo com perdas e data definida → comprometido | PATCH /batches/{id}/close; batch_service.transition_batch_state | Unidade | Particionamento de Equivalência (C1=T C2=T C3=T) | Retorna "comprometido" | current_state="ativo", has_losses=True, end_date_set=True. |
| TU-67 | RN-67: lote ativo sem data de conclusão → erro | PATCH /batches/{id}/close; batch_service.transition_batch_state | Unidade | Particionamento de Equivalência (C3=F) | Lança BatchStateError; 400 | current_state="ativo", end_date_set=False. |
| TU-68 | RN-68: lote já concluído não pode transicionar | PATCH /batches/{id}/close; batch_service.transition_batch_state | Unidade | Particionamento de Equivalência (estado terminal) | Lança BatchStateError; 400 | current_state="concluído". |
| TU-69 | RN-69: lote comprometido não pode transicionar | PATCH /batches/{id}/close; batch_service.transition_batch_state | Unidade | Particionamento de Equivalência (estado terminal) | Lança BatchStateError; 400 | current_state="comprometido". |
| TU-70 | RN-70: estado inválido ("suspenso") → erro imediato | PATCH /batches/{id}/close; batch_service.transition_batch_state | Unidade | Particionamento de Equivalência (estado desconhecido) | Lança BatchStateError; 400 | current_state="suspenso". |
| TU-71 | RN-71: sem perdas, colheita total → produtividade 100% | PATCH /batches/{id}/close; batch_service.calculate_productivity | Unidade | Particionamento de Equivalência (classe válida sem perdas) | Retorna 100.0 | planned_qty=100, actual_qty=100, losses=0. |
| TU-72 | RN-72: com perdas parciais → produtividade 80% | PATCH /batches/{id}/close; batch_service.calculate_productivity | Unidade | Particionamento de Equivalência (classe válida com perdas) | Retorna 80.0 | planned_qty=100, actual_qty=100, losses=20. |
| TU-73 | RN-73: colheita parcial sem perdas → produtividade 60% | PATCH /batches/{id}/close; batch_service.calculate_productivity | Unidade | Particionamento de Equivalência (colheita incompleta) | Retorna 60.0 | planned_qty=100, actual_qty=60, losses=0. |
| TU-74 | RN-74: perdas superiores à colheita → erro | PATCH /batches/{id}/close; batch_service.calculate_productivity | Unidade | Particionamento de Equivalência (losses > actual_qty) | Lança BatchCalculationError; 400 | planned_qty=100, actual_qty=50, losses=60. |
| TU-75 | RN-75: planned_qty = 0 → divisão por zero → erro | PATCH /batches/{id}/close; batch_service.calculate_productivity | Unidade | Valores Limite (planned_qty=0) | Lança BatchCalculationError; 400 | planned_qty=0. |
| TU-76 | RN-76: modo Automático + regra ativa + medição recente → executada | POST /automation/evaluate; automation_service.decide_automation | Unidade | Condições Múltiplas / MC/DC (C1=T C2=T C3=T) | Retorna "executada" | mode="Automático", rule_active=True, measurement_recent=True. |
| TU-77 | RN-77: modo Manual + regra ativa + medição recente → sugerida | POST /automation/evaluate; automation_service.decide_automation | Unidade | Condições Múltiplas / MC/DC (C1=F C2=T C3=T) | Retorna "sugerida" | mode="Manual", rule_active=True, measurement_recent=True. |
| TU-78 | RN-78: regra inativa → ignorada independentemente do modo | POST /automation/evaluate; automation_service.decide_automation | Unidade | Condições Múltiplas / MC/DC (C2=F) | Retorna "ignorada" | mode="Automático", rule_active=False, measurement_recent=True. |
| TU-79 | RN-79: medição não recente → ignorada independentemente do modo | POST /automation/evaluate; automation_service.decide_automation | Unidade | Condições Múltiplas / MC/DC (C3=F) | Retorna "ignorada" | mode="Manual", rule_active=True, measurement_recent=False. |
| TU-80 | RN-80: importação de CSV misto com 1 linha válida e 1 linha inválida (name vazio) | POST /herbs/import; herb_service.import_herbs_csv | Unidade | Particionamento de Equivalência (misto: uma linha válida juntamente com uma linha inválida) | result['imported']==1; result['failed']==1; catálogo tem 1 entrada | Catálogo vazio (reset_herbs). CSV com name="Lavanda" (válido) e name="" (inválido). |
| TU-81 | RN-81: tipo de plano "regular" é aceite | POST /plans; plan_service.validate_plan | Unidade | Particionamento de Equivalência (classe válida: regular) | validate_plan não lança; 201 | Nenhuma. Teste isolado com payload {"type":"regular"}. |
| TU-82 | RN-82: tipo de plano "emergência" é aceite | POST /plans; plan_service.validate_plan | Unidade | Particionamento de Equivalência (classe válida: emergência) | validate_plan não lança; 201 | Nenhuma. Teste isolado com payload {"type":"emergência"}. |
| TU-83 | RN-83: tipo de plano desconhecido é rejeitado | POST /plans; plan_service.validate_plan | Unidade | Particionamento de Equivalência (classe inválida: tipo desconhecido) | Lança PlanValidationError; 400 | Nenhuma. Teste isolado com payload {"type":"invalido"}. |
| TU-84 | RN-84: duração do ciclo de 0 dias rejeitada (abaixo do mínimo 1) | POST /plans; plan_service.validate_plan | Unidade | Análise de Valores Limite (days=0, abaixo do mínimo 1) | Lança PlanValidationError; 400 | Nenhuma. Teste isolado. |
| TU-85 | RN-85: duração do ciclo de 1 dia aceite (limite inferior exacto) | POST /plans; plan_service.validate_plan | Unidade | Análise de Valores Limite (days=1, limite inferior exacto) | validate_plan não lança; 201 | Nenhuma. Teste isolado. |
| TU-86 | RN-86: duração do ciclo de 90 dias aceite (valor nominal interior) | POST /plans; plan_service.validate_plan | Unidade | Análise de Valores Limite (days=90, valor nominal interior) | validate_plan não lança; 201 | Nenhuma. Teste isolado. |
| TU-87 | RN-87: duração do ciclo de 365 dias aceite (limite superior exacto) | POST /plans; plan_service.validate_plan | Unidade | Análise de Valores Limite (days=365, limite superior exacto) | validate_plan não lança; 201 | Nenhuma. Teste isolado. |
| TU-88 | RN-88: duração do ciclo de 366 dias rejeitada (acima do máximo 365) | POST /plans; plan_service.validate_plan | Unidade | Análise de Valores Limite (days=366, acima do máximo 365) | Lança PlanValidationError; 400 | Nenhuma. Teste isolado. |
| TU-89 | RN-89: resolução com action "resolvido" sem justificação → aceite | PATCH /alerts/{id}; alert_service.resolve_alert | Unidade | Particionamento de Equivalência (resolvido, justificação opcional ausente) | Retorna alerta com state="resolvido"; 200 | Alerta "pendente" inserido em memória (reset_alerts + add_alert). |
| TU-90 | RN-90: resolução com action "resolvido" com justificação → aceite | PATCH /alerts/{id}; alert_service.resolve_alert | Unidade | Particionamento de Equivalência (resolvido, justificação presente) | Retorna alerta com state="resolvido"; 200 | Alerta "pendente" inserido em memória. |
| TU-91 | RN-91: resolução com action "ignorado" e justificação válida (50 chars) → aceite | PATCH /alerts/{id}; alert_service.resolve_alert | Unidade | Particionamento de Equivalência (ignorado com justificação válida) | Retorna alerta com state="ignorado"; 200 | Alerta "pendente" inserido em memória. |
| TU-92 | RN-92: resolução com action "ignorado" sem justificação → rejeitada | PATCH /alerts/{id}; alert_service.resolve_alert | Unidade | Particionamento de Equivalência (ignorado sem justificação obrigatória) | Lança AlertActionError; 422 | Alerta "pendente" inserido em memória. |
| TU-93 | RN-93: resolução com action desconhecida ("cancelado") → rejeitada | PATCH /alerts/{id}; alert_service.resolve_alert | Unidade | Particionamento de Equivalência (action inválida) | Lança AlertActionError; 422 | Alerta "pendente" inserido em memória. |
| TU-94 | RN-94: justificação de 9 chars rejeitada (abaixo do mínimo 10) | PATCH /alerts/{id}; alert_service.resolve_alert | Unidade | Análise de Valores Limite (len=9, abaixo do mínimo 10) | Lança AlertActionError; 422 | Alerta "pendente" inserido em memória. |
| TU-95 | RN-95: justificação de 10 chars aceite (limite inferior exacto) | PATCH /alerts/{id}; alert_service.resolve_alert | Unidade | Análise de Valores Limite (len=10, limite inferior exacto) | Retorna alerta com state="ignorado"; 200 | Alerta "pendente" inserido em memória. |
| TU-96 | RN-96: justificação de 250 chars aceite (valor nominal interior) | PATCH /alerts/{id}; alert_service.resolve_alert | Unidade | Análise de Valores Limite (len=250, valor nominal) | Retorna alerta com state="ignorado"; 200 | Alerta "pendente" inserido em memória. |
| TU-97 | RN-97: justificação de 500 chars aceite (limite superior exacto) | PATCH /alerts/{id}; alert_service.resolve_alert | Unidade | Análise de Valores Limite (len=500, limite superior exacto) | Retorna alerta com state="ignorado"; 200 | Alerta "pendente" inserido em memória. |
| TU-98 | RN-98: justificação de 501 chars rejeitada (acima do máximo 500) | PATCH /alerts/{id}; alert_service.resolve_alert | Unidade | Análise de Valores Limite (len=501, acima do máximo 500) | Lança AlertActionError; 422 | Alerta "pendente" inserido em memória. |
| TU-99 | RN-99: resolução de alerta inexistente → AlertNotFoundError | PATCH /alerts/{id}; alert_service.resolve_alert | Unidade | Particionamento de Equivalência (id inexistente) | Lança AlertNotFoundError; 404 | Store de alertas vazio (reset_alerts). |
| TU-100 | RN-100: resolução de alerta já resolvido → AlertActionError | PATCH /alerts/{id}; alert_service.resolve_alert | Unidade | Particionamento de Equivalência (estado não "pendente") | Lança AlertActionError; 422 | Alerta com state="resolvido" inserido em memória. |
| TU-101 | RN-101: medição sem batch_id → MeasurementValidationError | POST /measurements; measurement_service.create_measurement | Unidade | Particionamento de Equivalência (campo obrigatório batch_id ausente) | Lança MeasurementValidationError; 400 | Nenhuma. Teste isolado. |
| TU-102 | RN-102: medição sem temp → MeasurementValidationError | POST /measurements; measurement_service.create_measurement | Unidade | Particionamento de Equivalência (campo obrigatório temp ausente) | Lança MeasurementValidationError; 400 | Nenhuma. Teste isolado. |
| TU-103 | RN-103: medição sem humidity → MeasurementValidationError | POST /measurements; measurement_service.create_measurement | Unidade | Particionamento de Equivalência (campo obrigatório humidity ausente) | Lança MeasurementValidationError; 400 | Nenhuma. Teste isolado. |
| TU-104 | RN-104: medição sem luminosity → MeasurementValidationError | POST /measurements; measurement_service.create_measurement | Unidade | Particionamento de Equivalência (campo obrigatório luminosity ausente) | Lança MeasurementValidationError; 400 | Nenhuma. Teste isolado. |
| TU-105 | RN-105: medição válida dentro dos limites → criada sem alerta | POST /measurements; measurement_service.create_measurement | Unidade | Particionamento de Equivalência (leituras dentro dos limites) | Retorna medição com alert=None; 201 | Lote ativo id=1 inserido em memória. Temp=23, hum=60, sensor_ok=True. |
| TU-106 | RN-106: medição com temperatura acima do limite e sensor ativo → alerta automático "Aviso" | POST /measurements; measurement_service.create_measurement | Unidade | Particionamento de Equivalência (temp > temp_max, sensor_ok=True) | Retorna medição com alert.level="Aviso"; 201 | Lote ativo id=1 inserido em memória. Temp=30 (>28), hum=60, sensor_ok=True. |

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
| RN-80: importação de CSV misto (válida + inválida) classifica corretamente | TU-80 |
| RN-81: tipo de plano "regular" é aceite | TU-81 |
| RN-82: tipo de plano "emergência" é aceite | TU-82 |
| RN-83: tipo de plano desconhecido é rejeitado | TU-83 |
| RN-84: duração do ciclo 0 dias rejeitada (abaixo do mínimo) | TU-84 |
| RN-85: duração do ciclo 1 dia aceite (limite inferior) | TU-85 |
| RN-86: duração do ciclo 90 dias aceite (valor nominal) | TU-86 |
| RN-87: duração do ciclo 365 dias aceite (limite superior) | TU-87 |
| RN-88: duração do ciclo 366 dias rejeitada (acima do máximo) | TU-88 |
| RN-89: resolve_alert "resolvido" sem justificação → aceite | TU-89 |
| RN-90: resolve_alert "resolvido" com justificação → aceite | TU-90 |
| RN-91: resolve_alert "ignorado" com justificação válida → aceite | TU-91 |
| RN-92: resolve_alert "ignorado" sem justificação → AlertActionError | TU-92 |
| RN-93: resolve_alert action inválida → AlertActionError | TU-93 |
| RN-94: justificação 9 chars rejeitada (abaixo do mínimo 10) | TU-94 |
| RN-95: justificação 10 chars aceite (limite inferior) | TU-95 |
| RN-96: justificação 250 chars aceite (valor nominal) | TU-96 |
| RN-97: justificação 500 chars aceite (limite superior) | TU-97 |
| RN-98: justificação 501 chars rejeitada (acima do máximo 500) | TU-98 |
| RN-99: resolve_alert id inexistente → AlertNotFoundError | TU-99 |
| RN-100: resolve_alert alerta não pendente → AlertActionError | TU-100 |
| RN-101: create_measurement sem batch_id → MeasurementValidationError | TU-101 |
| RN-102: create_measurement sem temp → MeasurementValidationError | TU-102 |
| RN-103: create_measurement sem humidity → MeasurementValidationError | TU-103 |
| RN-104: create_measurement sem luminosity → MeasurementValidationError | TU-104 |
| RN-105: create_measurement válida dentro dos limites → alert=None | TU-105 |
| RN-106: create_measurement com temp > limite e sensor ativo → alerta "Aviso" | TU-106 |

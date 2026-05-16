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
| TU-57 | RN-57: data no formato YYYY-MM-DD é aceite | POST /plans, /batches, /tasks; date_validator.validate_date | Unidade | Particionamento de Equivalência (formato válido) | validate_date não lança | Nenhuma. Teste isolado. |
| TU-58 | RN-58: data DD-MM-YYYY é rejeitada | POST /plans, /batches, /tasks; date_validator.validate_date | Unidade | Particionamento de Equivalência (DD-MM-YYYY inválido) | Lança DateValidationError; 400 | Nenhuma. Teste isolado. |
| TU-59 | RN-59: data MM-DD-YYYY é rejeitada | POST /plans, /batches, /tasks; date_validator.validate_date | Unidade | Particionamento de Equivalência (MM-DD-YYYY inválido) | Lança DateValidationError; 400 | Nenhuma. Teste isolado. |
| TU-60 | RN-60: data DD/MM/YYYY com barras é rejeitada | POST /plans, /batches, /tasks; date_validator.validate_date | Unidade | Particionamento de Equivalência (barras em vez de hífens) | Lança DateValidationError; 400 | Nenhuma. Teste isolado. |
| TU-61 | RN-61: data YYYY/MM/DD com barras é rejeitada | POST /plans, /batches, /tasks; date_validator.validate_date | Unidade | Particionamento de Equivalência (barras em vez de hífens) | Lança DateValidationError; 400 | Nenhuma. Teste isolado. |
| TU-62 | RN-62: data sem separadores (YYYYMMDD) é rejeitada | POST /plans, /batches, /tasks; date_validator.validate_date | Unidade | Particionamento de Equivalência (sem separadores) | Lança DateValidationError; 400 | Nenhuma. Teste isolado. |
| TU-63 | RN-63: string que não é data é rejeitada | POST /plans, /batches, /tasks; date_validator.validate_date | Unidade | Particionamento de Equivalência (string não-data) | Lança DateValidationError; 400 | Nenhuma. Teste isolado. |
| TU-64 | RN-64: data por extenso é rejeitada | POST /plans, /batches, /tasks; date_validator.validate_date | Unidade | Particionamento de Equivalência (data por extenso) | Lança DateValidationError; 400 | Nenhuma. Teste isolado. |
| TU-65 | RN-65: mês inexistente (2026-13-01) é rejeitado | POST /plans, /batches, /tasks; date_validator.validate_date | Unidade | Particionamento de Equivalência (mês inválido) | Lança DateValidationError; 400 | Nenhuma. Teste isolado. |
| TU-66 | RN-66: dia inexistente (2026-02-30) é rejeitado | POST /plans, /batches, /tasks; date_validator.validate_date | Unidade | Particionamento de Equivalência (dia inválido) | Lança DateValidationError; 400 | Nenhuma. Teste isolado. |
| TU-67 | RN-67: lote ativo sem perdas com data definida transiciona para concluído | PATCH /batches/{id}/close; batch_service.transition_batch_state | Unidade | Particionamento de Equivalência | Retorna "concluído" | current_state="ativo", has_losses=False, end_date_set=True. |
| TU-68 | RN-68: lote ativo com perdas e data definida transiciona para comprometido | PATCH /batches/{id}/close; batch_service.transition_batch_state | Unidade | Particionamento de Equivalência | Retorna "comprometido" | current_state="ativo", has_losses=True, end_date_set=True. |
| TU-69 | RN-69: lote ativo sem data de conclusão lança erro | PATCH /batches/{id}/close; batch_service.transition_batch_state | Unidade | Particionamento de Equivalência (end_date_set=False) | Lança BatchStateError; 400 | current_state="ativo", end_date_set=False. |
| TU-70 | RN-70: lote já concluído não pode transicionar | PATCH /batches/{id}/close; batch_service.transition_batch_state | Unidade | Particionamento de Equivalência (estado terminal) | Lança BatchStateError; 400 | current_state="concluído". |
| TU-71 | RN-71: lote comprometido não pode transicionar | PATCH /batches/{id}/close; batch_service.transition_batch_state | Unidade | Particionamento de Equivalência (estado terminal) | Lança BatchStateError; 400 | current_state="comprometido". |
| TU-72 | RN-72: estado inválido lança erro imediato | PATCH /batches/{id}/close; batch_service.transition_batch_state | Unidade | Particionamento de Equivalência (estado desconhecido) | Lança BatchStateError; 400 | current_state="suspenso". |
| TU-73 | RN-73: sem perdas, colheita total — produtividade 100% | PATCH /batches/{id}/close; batch_service.calculate_productivity | Unidade | Particionamento de Equivalência (sem perdas) | Retorna 100.0 | planned=100, actual=100, losses=0. |
| TU-74 | RN-74: com perdas parciais — produtividade 80% | PATCH /batches/{id}/close; batch_service.calculate_productivity | Unidade | Particionamento de Equivalência (com perdas) | Retorna 80.0 | planned=100, actual=100, losses=20. |
| TU-75 | RN-75: colheita parcial sem perdas — produtividade 60% | PATCH /batches/{id}/close; batch_service.calculate_productivity | Unidade | Particionamento de Equivalência (colheita incompleta) | Retorna 60.0 | planned=100, actual=60, losses=0. |
| TU-76 | RN-76: perdas superiores à colheita lançam erro | PATCH /batches/{id}/close; batch_service.calculate_productivity | Unidade | Particionamento de Equivalência (losses > actual) | Lança BatchCalculationError; 400 | planned=100, actual=50, losses=60. |
| TU-77 | RN-77: planned_qty=0 lança erro de divisão | PATCH /batches/{id}/close; batch_service.calculate_productivity | Unidade | Particionamento de Equivalência (planned=0) | Lança BatchCalculationError; 400 | planned=0. |
| TU-78 | RN-78: criação de lote com payload válido é aceite | POST /batches; batch_service.validate_batch | Unidade | Particionamento de Equivalência (classe válida) | validate_batch não lança; 201 | Nenhuma. Teste isolado com herb_id=1, planned_qty=100. |
| TU-79 | RN-79: criação de lote sem herb_id lança erro | POST /batches; batch_service.validate_batch | Unidade | Particionamento de Equivalência (herb_id ausente) | Lança BatchValidationError; 400 | Nenhuma. Teste isolado. |
| TU-80 | RN-80: criação de lote com planned_qty=0 lança erro | POST /batches; batch_service.validate_batch | Unidade | Particionamento de Equivalência (planned_qty zero) | Lança BatchValidationError; 400 | Nenhuma. Teste isolado. |
| TU-81 | RN-81: criação de lote com planned_qty negativo lança erro | POST /batches; batch_service.validate_batch | Unidade | Particionamento de Equivalência (planned_qty negativo) | Lança BatchValidationError; 400 | Nenhuma. Teste isolado. |
| TU-82 | RN-82: tarefa do tipo rega é aceite | POST /tasks; task_service.validate_task | Unidade | Particionamento de Equivalência (classe válida) | validate_task não lança; 201 | Nenhuma. Teste isolado. |
| TU-83 | RN-83: tarefa do tipo fertilização é aceite | POST /tasks; task_service.validate_task | Unidade | Particionamento de Equivalência (classe válida) | validate_task não lança; 201 | Nenhuma. Teste isolado. |
| TU-84 | RN-84: tarefa do tipo colheita é aceite | POST /tasks; task_service.validate_task | Unidade | Particionamento de Equivalência (classe válida) | validate_task não lança; 201 | Nenhuma. Teste isolado. |
| TU-85 | RN-85: tarefa do tipo monitorização é aceite | POST /tasks; task_service.validate_task | Unidade | Particionamento de Equivalência (classe válida) | validate_task não lança; 201 | Nenhuma. Teste isolado. |
| TU-86 | RN-86: tarefa do tipo desconhecido é rejeitada | POST /tasks; task_service.validate_task | Unidade | Particionamento de Equivalência (classe inválida) | Lança TaskValidationError; 400 | Nenhuma. Teste isolado. |
| TU-87 | RN-87: tarefa sem batch_id lança erro | POST /tasks; task_service.validate_task | Unidade | Particionamento de Equivalência (batch_id ausente) | Lança TaskValidationError; 400 | Nenhuma. Teste isolado. |
| TU-88 | RN-88: tarefa sem task_type lança erro | POST /tasks; task_service.validate_task | Unidade | Particionamento de Equivalência (task_type ausente) | Lança TaskValidationError; 400 | Nenhuma. Teste isolado. |
| TU-89 | RN-89: tarefa com data em formato inválido DD-MM-YYYY lança erro | POST /tasks; task_service.validate_task | Unidade | Particionamento de Equivalência (formato de data inválido) | Lança TaskValidationError; 400 | Nenhuma. Teste isolado. |
| TU-90 | RN-90: medição com temp=17°C (abaixo de 18) gera alerta | POST /measurements; measurement_service.create_measurement | Unidade | Análise de Valores Limite (temp=17, abaixo do mínimo 18) | result["alert"] não é None | Lote ativo id=1 em memória. |
| TU-91 | RN-91: medição com temp=18°C (limite inferior) não gera alerta | POST /measurements; measurement_service.create_measurement | Unidade | Análise de Valores Limite (temp=18, limite inferior exacto) | result["alert"] é None | Lote ativo id=1 em memória. |
| TU-92 | RN-92: medição com temp=23°C (nominal) não gera alerta | POST /measurements; measurement_service.create_measurement | Unidade | Análise de Valores Limite (temp=23, valor nominal interior) | result["alert"] é None | Lote ativo id=1 em memória. |
| TU-93 | RN-93: medição com temp=28°C (limite superior) não gera alerta | POST /measurements; measurement_service.create_measurement | Unidade | Análise de Valores Limite (temp=28, limite superior exacto) | result["alert"] é None | Lote ativo id=1 em memória. |
| TU-94 | RN-94: medição com temp=29°C (acima de 28) gera alerta | POST /measurements; measurement_service.create_measurement | Unidade | Análise de Valores Limite (temp=29, acima do máximo 28) | result["alert"] não é None | Lote ativo id=1 em memória. |
| TU-95 | RN-95: medição com hum=39% (abaixo de 40) gera alerta | POST /measurements; measurement_service.create_measurement | Unidade | Análise de Valores Limite (hum=39, abaixo do mínimo 40) | result["alert"] não é None | Lote ativo id=1 em memória. |
| TU-96 | RN-96: medição com hum=40% (limite inferior) não gera alerta | POST /measurements; measurement_service.create_measurement | Unidade | Análise de Valores Limite (hum=40, limite inferior exacto) | result["alert"] é None | Lote ativo id=1 em memória. |
| TU-97 | RN-97: medição com hum=60% (nominal) não gera alerta | POST /measurements; measurement_service.create_measurement | Unidade | Análise de Valores Limite (hum=60, valor nominal interior) | result["alert"] é None | Lote ativo id=1 em memória. |
| TU-98 | RN-98: medição com hum=80% (limite superior) não gera alerta | POST /measurements; measurement_service.create_measurement | Unidade | Análise de Valores Limite (hum=80, limite superior exacto) | result["alert"] é None | Lote ativo id=1 em memória. |
| TU-99 | RN-99: medição com hum=81% (acima de 80) gera alerta | POST /measurements; measurement_service.create_measurement | Unidade | Análise de Valores Limite (hum=81, acima do máximo 80) | result["alert"] não é None | Lote ativo id=1 em memória. |
| TU-100 | RN-100: medição com lux=4999 (abaixo de 5000) gera alerta Informativo | POST /measurements; measurement_service.create_measurement | Unidade | Análise de Valores Limite (lux=4999, abaixo do mínimo 5000) | result["alert"].level=="Informativo" | Lote ativo id=1 em memória. |
| TU-101 | RN-101: medição com lux=5000 (limite inferior) não gera alerta | POST /measurements; measurement_service.create_measurement | Unidade | Análise de Valores Limite (lux=5000, limite inferior exacto) | result["alert"] é None | Lote ativo id=1 em memória. |
| TU-102 | RN-102: medição com lux=15000 (nominal) não gera alerta | POST /measurements; measurement_service.create_measurement | Unidade | Análise de Valores Limite (lux=15000, valor nominal interior) | result["alert"] é None | Lote ativo id=1 em memória. |
| TU-103 | RN-103: medição com lux=25000 (limite superior) não gera alerta | POST /measurements; measurement_service.create_measurement | Unidade | Análise de Valores Limite (lux=25000, limite superior exacto) | result["alert"] é None | Lote ativo id=1 em memória. |
| TU-104 | RN-104: medição com lux=25001 (acima de 25000) gera alerta Informativo | POST /measurements; measurement_service.create_measurement | Unidade | Análise de Valores Limite (lux=25001, acima do máximo 25000) | result["alert"].level=="Informativo" | Lote ativo id=1 em memória. |
| TU-105 | RN-105: sensor_ok=False — sem alerta mesmo com leituras fora dos limites | POST /measurements; measurement_service.create_measurement | Unidade | Particionamento de Equivalência (sensor desligado) | result["alert"] é None | Lote ativo id=1 em memória. |
| TU-106 | RN-106: sensor_ok não booleano lança MeasurementValidationError | POST /measurements; measurement_service.create_measurement | Unidade | Particionamento de Equivalência (sensor_ok tipo inválido) | Lança MeasurementValidationError; 400 | Nenhuma. Teste isolado. |
| TU-107 | RN-107: todas leituras normais e sensor activo — sem alerta | POST /measurements; alert_service.classify_alert | Unidade | Particionamento de Equivalência (classe None) | Retorna None | temp=23, hum=60, lux=15000, sensor_ok=True. |
| TU-108 | RN-108: temperatura alta (29°C) — Aviso | POST /measurements; alert_service.classify_alert | Unidade | Particionamento de Equivalência (classe Aviso — temp alta) | Retorna "Aviso" | temp=29, hum=60, lux=15000, sensor_ok=True. |
| TU-109 | RN-109: temperatura baixa (17°C) — Aviso | POST /measurements; alert_service.classify_alert | Unidade | Particionamento de Equivalência (classe Aviso — temp baixa) | Retorna "Aviso" | temp=17, hum=60, lux=15000, sensor_ok=True. |
| TU-110 | RN-110: humidade alta (85%) — Aviso | POST /measurements; alert_service.classify_alert | Unidade | Particionamento de Equivalência (classe Aviso — hum alta) | Retorna "Aviso" | temp=23, hum=85, lux=15000, sensor_ok=True. |
| TU-111 | RN-111: humidade baixa (35%) — Aviso | POST /measurements; alert_service.classify_alert | Unidade | Particionamento de Equivalência (classe Aviso — hum baixa) | Retorna "Aviso" | temp=23, hum=35, lux=15000, sensor_ok=True. |
| TU-112 | RN-112: temp e hum ambas fora dos limites — Crítico | POST /measurements; alert_service.classify_alert | Unidade | Particionamento de Equivalência (classe Crítico) | Retorna "Crítico" | temp=29, hum=35, lux=15000, sensor_ok=True. |
| TU-113 | RN-113: luminosidade fora dos limites — Informativo | POST /measurements; alert_service.classify_alert | Unidade | Particionamento de Equivalência (classe Informativo) | Retorna "Informativo" | temp=23, hum=60, lux=26000, sensor_ok=True. |
| TU-114 | RN-114: sensor desligado — sem alerta independentemente das leituras | POST /measurements; alert_service.classify_alert | Unidade | Particionamento de Equivalência (sensor_ok=False) | Retorna None | temp=29, hum=35, lux=26000, sensor_ok=False. |
| TU-115 | RN-115: resolução com action resolvido sem justificação é aceite | PATCH /alerts/{id}; alert_service.resolve_alert | Unidade | Particionamento de Equivalência (resolvido, justificação opcional ausente) | Retorna alerta com state="resolvido"; 200 | Alerta pendente em memória. |
| TU-116 | RN-116: resolução com action resolvido com justificação é aceite | PATCH /alerts/{id}; alert_service.resolve_alert | Unidade | Particionamento de Equivalência (resolvido com justificação presente) | Retorna alerta com state="resolvido"; 200 | Alerta pendente em memória. |
| TU-117 | RN-117: resolução com action ignorado e justificação válida é aceite | PATCH /alerts/{id}; alert_service.resolve_alert | Unidade | Particionamento de Equivalência (ignorado com justificação válida) | Retorna alerta com state="ignorado"; 200 | Alerta pendente em memória. |
| TU-118 | RN-118: resolução com action ignorado sem justificação é rejeitada | PATCH /alerts/{id}; alert_service.resolve_alert | Unidade | Particionamento de Equivalência (ignorado sem justificação obrigatória) | Lança AlertActionError; 422 | Alerta pendente em memória. |
| TU-119 | RN-119: resolução com action desconhecida é rejeitada | PATCH /alerts/{id}; alert_service.resolve_alert | Unidade | Particionamento de Equivalência (action inválida) | Lança AlertActionError; 422 | Alerta pendente em memória. |
| TU-120 | RN-120: justificação de 9 chars rejeitada (abaixo do mínimo 10) | PATCH /alerts/{id}; alert_service.resolve_alert | Unidade | Análise de Valores Limite (len=9, abaixo do mínimo 10) | Lança AlertActionError; 422 | Alerta pendente em memória. |
| TU-121 | RN-121: justificação de 10 chars aceite (limite inferior exacto) | PATCH /alerts/{id}; alert_service.resolve_alert | Unidade | Análise de Valores Limite (len=10, limite inferior exacto) | Retorna alerta com state="ignorado"; 200 | Alerta pendente em memória. |
| TU-122 | RN-122: justificação de 250 chars aceite (valor nominal interior) | PATCH /alerts/{id}; alert_service.resolve_alert | Unidade | Análise de Valores Limite (len=250, valor nominal) | Retorna alerta com state="ignorado"; 200 | Alerta pendente em memória. |
| TU-123 | RN-123: justificação de 500 chars aceite (limite superior exacto) | PATCH /alerts/{id}; alert_service.resolve_alert | Unidade | Análise de Valores Limite (len=500, limite superior exacto) | Retorna alerta com state="ignorado"; 200 | Alerta pendente em memória. |
| TU-124 | RN-124: justificação de 501 chars rejeitada (acima do máximo 500) | PATCH /alerts/{id}; alert_service.resolve_alert | Unidade | Análise de Valores Limite (len=501, acima do máximo 500) | Lança AlertActionError; 422 | Alerta pendente em memória. |
| TU-125 | RN-125: resolução de alerta com id inexistente lança AlertNotFoundError | PATCH /alerts/{id}; alert_service.resolve_alert | Unidade | Particionamento de Equivalência (id inexistente) | Lança AlertNotFoundError; 404 | Store de alertas vazio. |
| TU-126 | RN-126: resolução de alerta já resolvido lança AlertActionError | PATCH /alerts/{id}; alert_service.resolve_alert | Unidade | Particionamento de Equivalência (estado não pendente) | Lança AlertActionError; 422 | Alerta com state="resolvido" em memória. |
| TU-127 | RN-127: modo Automático + regra ativa + medição recente — executada | POST /automation/evaluate; automation_service.decide_automation | Unidade | Particionamento de Equivalência (classe executada) | Retorna "executada" | mode="Automático", rule_active=True, measurement_recent=True. |
| TU-128 | RN-128: modo Manual + regra ativa + medição recente — sugerida | POST /automation/evaluate; automation_service.decide_automation | Unidade | Particionamento de Equivalência (classe sugerida) | Retorna "sugerida" | mode="Manual", rule_active=True, measurement_recent=True. |
| TU-129 | RN-129: regra inativa — ignorada independentemente do modo | POST /automation/evaluate; automation_service.decide_automation | Unidade | Particionamento de Equivalência (regra inativa) | Retorna "ignorada" | mode="Automático", rule_active=False. |
| TU-130 | RN-130: medição não recente — ignorada independentemente do modo | POST /automation/evaluate; automation_service.decide_automation | Unidade | Particionamento de Equivalência (medição não recente) | Retorna "ignorada" | mode="Manual", measurement_recent=False. |
| TU-131 | RN-131: modo inválido lança AutomationDecisionError | POST /automation/evaluate; automation_service.decide_automation | Unidade | Particionamento de Equivalência (modo inválido) | Lança AutomationDecisionError; 400 | Nenhuma. Teste isolado. |
| TU-132 | RN-132: perfil Técnico é aceite | POST /users; user_service.validate_user | Unidade | Particionamento de Equivalência (perfil válido) | validate_user não lança; 201 | Nenhuma. Teste isolado. |
| TU-133 | RN-133: perfil Responsável Técnico é aceite | POST /users; user_service.validate_user | Unidade | Particionamento de Equivalência (perfil válido) | validate_user não lança; 201 | Nenhuma. Teste isolado. |
| TU-134 | RN-134: perfil Administrador é aceite | POST /users; user_service.validate_user | Unidade | Particionamento de Equivalência (perfil válido) | validate_user não lança; 201 | Nenhuma. Teste isolado. |
| TU-135 | RN-135: perfil Gestor (desconhecido) é rejeitado | POST /users; user_service.validate_user | Unidade | Particionamento de Equivalência (perfil inválido) | Lança UserValidationError; 400 | Nenhuma. Teste isolado. |
| TU-136 | RN-136: perfil null é rejeitado | POST /users; user_service.validate_user | Unidade | Particionamento de Equivalência (perfil ausente) | Lança UserValidationError; 400 | Nenhuma. Teste isolado. |
| TU-137 | RN-137: payload válido completo é aceite | POST /users; user_service.validate_user | Unidade | Particionamento de Equivalência (classe válida) | validate_user não lança; 201 | Nenhuma. Teste isolado. |
| TU-138 | RN-138: username em falta lança UserValidationError | POST /users; user_service.validate_user | Unidade | Particionamento de Equivalência (username ausente) | Lança UserValidationError; 400 | Nenhuma. Teste isolado. |
| TU-139 | RN-139: password em falta lança UserValidationError | POST /users; user_service.validate_user | Unidade | Particionamento de Equivalência (password ausente) | Lança UserValidationError; 400 | Nenhuma. Teste isolado. |
| TU-140 | RN-140: role em falta lança UserValidationError | POST /users; user_service.validate_user | Unidade | Particionamento de Equivalência (role ausente) | Lança UserValidationError; 400 | Nenhuma. Teste isolado. |
| TU-141 | RN-141: username vazio lança UserValidationError | POST /users; user_service.validate_user | Unidade | Particionamento de Equivalência (username vazio) | Lança UserValidationError; 400 | Nenhuma. Teste isolado. |
| TU-142 | RN-142: formato CSV é aceite | GET /reports; report_service.validate_report_format | Unidade | Particionamento de Equivalência (formato válido) | validate_report_format não lança; 200 | Nenhuma. Teste isolado. |
| TU-143 | RN-143: formato Excel é aceite | GET /reports; report_service.validate_report_format | Unidade | Particionamento de Equivalência (formato válido) | validate_report_format não lança; 200 | Nenhuma. Teste isolado. |
| TU-144 | RN-144: formato PDF é rejeitado | GET /reports; report_service.validate_report_format | Unidade | Particionamento de Equivalência (formato inválido) | Lança ReportValidationError; 400 | Nenhuma. Teste isolado. |
| TU-145 | RN-145: formato JSON é rejeitado | GET /reports; report_service.validate_report_format | Unidade | Particionamento de Equivalência (formato inválido) | Lança ReportValidationError; 400 | Nenhuma. Teste isolado. |
| TU-146 | RN-146: formato null é rejeitado | GET /reports; report_service.validate_report_format | Unidade | Particionamento de Equivalência (formato ausente) | Lança ReportValidationError; 400 | Nenhuma. Teste isolado. |
| TU-147 | RN-147: operação create_batch é auditável | GET /audit; audit_service.is_auditable_action | Unidade | Particionamento de Equivalência (operação de escrita) | Retorna True | Nenhuma. Teste isolado. |
| TU-148 | RN-148: operação resolve_alert é auditável | GET /audit; audit_service.is_auditable_action | Unidade | Particionamento de Equivalência (operação de escrita) | Retorna True | Nenhuma. Teste isolado. |
| TU-149 | RN-149: operação close_batch é auditável | GET /audit; audit_service.is_auditable_action | Unidade | Particionamento de Equivalência (operação de escrita) | Retorna True | Nenhuma. Teste isolado. |
| TU-150 | RN-150: operação get_batches não é auditável | GET /audit; audit_service.is_auditable_action | Unidade | Particionamento de Equivalência (operação de leitura) | Retorna False | Nenhuma. Teste isolado. |
| TU-151 | RN-151: operação get_herbs não é auditável | GET /audit; audit_service.is_auditable_action | Unidade | Particionamento de Equivalência (operação de leitura) | Retorna False | Nenhuma. Teste isolado. |

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
| RN-57 | TU-57 |
| RN-58 | TU-58 |
| RN-59 | TU-59 |
| RN-60 | TU-60 |
| RN-61 | TU-61 |
| RN-62 | TU-62 |
| RN-63 | TU-63 |
| RN-64 | TU-64 |
| RN-65 | TU-65 |
| RN-66 | TU-66 |
| RN-67 | TU-67 |
| RN-68 | TU-68 |
| RN-69 | TU-69 |
| RN-70 | TU-70 |
| RN-71 | TU-71 |
| RN-72 | TU-72 |
| RN-73 | TU-73 |
| RN-74 | TU-74 |
| RN-75 | TU-75 |
| RN-76 | TU-76 |
| RN-77 | TU-77 |
| RN-78 | TU-78 |
| RN-79 | TU-79 |
| RN-80 | TU-80 |
| RN-81 | TU-81 |
| RN-82 | TU-82 |
| RN-83 | TU-83 |
| RN-84 | TU-84 |
| RN-85 | TU-85 |
| RN-86 | TU-86 |
| RN-87 | TU-87 |
| RN-88 | TU-88 |
| RN-89 | TU-89 |
| RN-90 | TU-90 |
| RN-91 | TU-91 |
| RN-92 | TU-92 |
| RN-93 | TU-93 |
| RN-94 | TU-94 |
| RN-95 | TU-95 |
| RN-96 | TU-96 |
| RN-97 | TU-97 |
| RN-98 | TU-98 |
| RN-99 | TU-99 |
| RN-100 | TU-100 |
| RN-101 | TU-101 |
| RN-102 | TU-102 |
| RN-103 | TU-103 |
| RN-104 | TU-104 |
| RN-105 | TU-105 |
| RN-106 | TU-106 |
| RN-107 | TU-107 |
| RN-108 | TU-108 |
| RN-109 | TU-109 |
| RN-110 | TU-110 |
| RN-111 | TU-111 |
| RN-112 | TU-112 |
| RN-113 | TU-113 |
| RN-114 | TU-114 |
| RN-115 | TU-115 |
| RN-116 | TU-116 |
| RN-117 | TU-117 |
| RN-118 | TU-118 |
| RN-119 | TU-119 |
| RN-120 | TU-120 |
| RN-121 | TU-121 |
| RN-122 | TU-122 |
| RN-123 | TU-123 |
| RN-124 | TU-124 |
| RN-125 | TU-125 |
| RN-126 | TU-126 |
| RN-127 | TU-127 |
| RN-128 | TU-128 |
| RN-129 | TU-129 |
| RN-130 | TU-130 |
| RN-131 | TU-131 |
| RN-132 | TU-132 |
| RN-133 | TU-133 |
| RN-134 | TU-134 |
| RN-135 | TU-135 |
| RN-136 | TU-136 |
| RN-137 | TU-137 |
| RN-138 | TU-138 |
| RN-139 | TU-139 |
| RN-140 | TU-140 |
| RN-141 | TU-141 |
| RN-142 | TU-142 |
| RN-143 | TU-143 |
| RN-144 | TU-144 |
| RN-145 | TU-145 |
| RN-146 | TU-146 |
| RN-147 | TU-147 |
| RN-148 | TU-148 |
| RN-149 | TU-149 |
| RN-150 | TU-150 |
| RN-151 | TU-151 |

# Matriz de Rastreabilidade

| ID | Requisito / Regra | Endpoint | Nível | Técnica | Resultado Esperado | Pré-condições |
| --- | --- | --- | --- | --- | --- | --- |
| TU-01 | RN-01: autenticação com username correto e password correta | prefix /auth; POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Retorna utilizador sem password; 200 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-02 | RN-02: rejeita username correto com password errada | prefix /auth; POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Retorna None; 401 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-03 | RN-03: rejeita username correto com password vazia | prefix /auth; POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Lança AuthInputValidationError; 400 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-04 | RN-04: rejeita username correto com password null | prefix /auth; POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Lança AuthInputValidationError; 400 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-05 | RN-05: rejeita username correto com password só com espaços | prefix /auth; POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Lança AuthInputValidationError; 400 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-06 | RN-06: rejeita username correto com password demasiado longa | prefix /auth; POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Lança AuthInputValidationError; 400 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-07 | RN-07: rejeita username correto com password com caracteres especiais | prefix /auth; POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Lança AuthInputValidationError; 400 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-08 | RN-08: rejeita username inexistente com password correta | prefix /auth; POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Retorna None; 401 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-09 | RN-09: rejeita username inexistente com password errada | prefix /auth; POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Retorna None; 401 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-10 | RN-10: rejeita username vazio com password correta | prefix /auth; POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Lança AuthInputValidationError; 400 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-11 | RN-11: rejeita username vazio com password vazia | prefix /auth; POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Lança AuthInputValidationError; 400 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-12 | RN-12: rejeita username null com password correta | prefix /auth; POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Lança AuthInputValidationError; 400 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-13 | RN-13: rejeita username null com password null | prefix /auth; POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Lança AuthInputValidationError; 400 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-14 | RN-14: rejeita username só com espaços com password correta | prefix /auth; POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Lança AuthInputValidationError; 400 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-15 | RN-15: rejeita username demasiado longo com password correta | prefix /auth; POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Lança AuthInputValidationError; 400 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-16 | RN-16: rejeita username com caracteres especiais com password correta | prefix /auth; POST /login; auth_service.authenticate_user | Unidade | Particionamento de Equivalência | Lança AuthInputValidationError; 400 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-17 | RN-17: emite access token para utilizador válido | prefix /auth; POST /login; auth_service.generate_token | Unidade | Particionamento de Equivalência | Retorna JWT access com id, username, role, type e exp; 200 | Utilizador admin autenticado em memória. |
| TU-18 | RN-18: emite refresh token para utilizador válido | prefix /auth; POST /login; auth_service.generate_token | Unidade | Particionamento de Equivalência | Retorna JWT refresh com id, username, role, type e exp; 200 | Utilizador admin autenticado em memória. |
| TU-19 | RN-19: rejeita emissão de token sem utilizador | prefix /auth; POST /login; auth_service.generate_token | Unidade | Particionamento de Equivalência | Lança ValueError; 400 equivalente | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-20 | RN-20: rejeita emissão de token com tipo inválido | prefix /auth; POST /login; auth_service.generate_token | Unidade | Particionamento de Equivalência | Lança ValueError; 400 equivalente | Utilizador admin autenticado em memória. |
| TU-21 | RN-21: descodifica access token válido | prefix /auth; token validation; auth_service.decode_token | Unidade | Particionamento de Equivalência | Retorna payload correto; 200 | Access token admin gerado. |
| TU-22 | RN-22: rejeita access token quando é esperado refresh | prefix /auth; POST /refresh; auth_service.decode_token | Unidade | Particionamento de Equivalência | Lança TokenValidationError; 401 | Access token admin gerado. |
| TU-23 | RN-23: rejeita token malformado | prefix /auth; token validation; auth_service.decode_token | Unidade | Particionamento de Equivalência | Lança TokenValidationError; 401 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-24 | RN-24: rejeita token vazio | prefix /auth; token validation; auth_service.decode_token | Unidade | Particionamento de Equivalência | Lança TokenValidationError; 401 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-25 | RN-25: rejeita token null | prefix /auth; token validation; auth_service.decode_token | Unidade | Particionamento de Equivalência | Lança TokenValidationError; 401 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-26 | RN-26: rejeita token adulterado | prefix /auth; token validation; auth_service.decode_token | Unidade | Particionamento de Equivalência | Lança TokenValidationError; 401 | Token válido gerado e assinatura alterada. |
| TU-27 | RN-27: rejeita token expirado | prefix /auth; token validation; auth_service.decode_token | Unidade | Particionamento de Equivalência | Lança TokenValidationError; 401 | Token criado com expiração no passado. |
| TU-28 | RN-28: renova refresh token válido | prefix /auth; POST /refresh; auth_service.refresh_token | Unidade | Particionamento de Equivalência | Retorna novo access_token e refresh_token; 200 | Refresh token admin válido e registado em memória. |
| TU-29 | RN-29: rejeita refresh token expirado | prefix /auth; POST /refresh; auth_service.refresh_token | Unidade | Particionamento de Equivalência | Lança TokenValidationError; 401 | Refresh token criado com expiração no passado. |
| TU-30 | RN-30: rejeita refresh token malformado | prefix /auth; POST /refresh; auth_service.refresh_token | Unidade | Particionamento de Equivalência | Lança TokenValidationError; 401 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-31 | RN-31: rejeita refresh token vazio | prefix /auth; POST /refresh; auth_service.refresh_token | Unidade | Particionamento de Equivalência | Lança TokenValidationError; 401 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-32 | RN-32: rejeita refresh token null | prefix /auth; POST /refresh; auth_service.refresh_token | Unidade | Particionamento de Equivalência | Lança TokenValidationError; 401 | Nenhuma. Teste isolado sem dependências de BD ou rede. |
| TU-33 | RN-33: rejeita refresh token válido mas não registado | prefix /auth; POST /refresh; auth_service.refresh_token | Unidade | Particionamento de Equivalência | Retorna None; 401 | Refresh token válido gerado e removido do store em memória. |
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

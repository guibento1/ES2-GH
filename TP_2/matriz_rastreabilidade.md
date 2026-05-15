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

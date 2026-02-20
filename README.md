# CNABEngine

CNABEngine é um projeto em Python para **validação e processamento de arquivos CNAB**  
(Foco inicial: CNAB 400).

O projeto atualmente possui **duas formas de execução**:
- ✅ Execução via **terminal (CLI)**
- ✅ Execução via **interface web (Flask)**

---

## 🎯 Objetivo

Fornecer uma engine simples, extensível e reutilizável para:

- Validar estrutura de arquivos CNAB
- Garantir tamanho de linhas (400 posições)
- Verificar registros Header, Detail e Trailer
- Validar sequência de registros
- Preparar base para parsing futuro
- Disponibilizar interface web para upload e validação

---

## 🧩 Funcionalidades

- [x] Leitura de arquivo texto
- [x] Validação de tamanho da linha (CNAB 400)
- [x] Validação estrutural básica
- [x] Execução via terminal (CLI)
- [x] Interface web para upload de arquivo
- [ ] Validação completa de registros obrigatórios
- [ ] Suporte a múltiplos layouts
- [ ] Testes automatizados com pytest

---

## 🛠️ Tecnologias

- Python 3.10+
- Flask (Interface Web)
- Estrutura modular
- Testes com pytest (planejado)

---

## ▶️ Como Executar

### 🔹 1️⃣ Execução via Terminal (CLI)

Validação direta pelo terminal:

```bash
python main.py caminho/do/arquivo.txt

Exemplo:
python main.py examples/remessa.txt
```
### 🔹 2️⃣ Execução via Interface Web

Inicia o servidor Flask:
```bash
python app.py

Depois acesse no navegador:
http://localhost:5000

Na interface será possível:
 - Fazer upload de arquivo CNAB
 - Validar estrutura
 - Visualizar erros encontrados
```
## 📂 Estrutura do Projeto
```bash
CNABEngine/
├── cnabengine/        # Código-fonte principal
│   ├── core/          # Regras de validação
│   ├── layouts/       # Definições de layouts CNAB
│   └── utils/         # Funções utilitárias
├── templates/         # HTML da interface Flask
├── static/            # CSS / JS
├── tests/             # Testes automatizados
├── examples/          # Arquivos de exemplo
├── main.py            # Execução via terminal
├── app.py             # Execução via interface web
└── README.md
```

## ⚠️ Observações

Projeto em fase inicial de desenvolvimento
- Estrutura sujeita a mudanças
- Foco atual em validação CNAB 400
- Ainda não há persistência em banco de dados
- Pode ser executado via CLI ou Web

## 📄 Licença
Este projeto está licenciado sob a licença MIT.
Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
# CNABEngine

CNABEngine é um projeto em Python para **validação e processamento de arquivos CNAB**  
(Foco inicial: CNAB 400).

## 🎯 Objetivo
Fornecer uma engine simples, extensível e reutilizável para:
- Validar estrutura de arquivos CNAB
- Garantir tamanho de linhas
- Verificar registros Header, Detail e Trailer
- Preparar base para parsing futuro

## 🧩 Funcionalidades (em desenvolvimento)
- [x] Leitura de arquivo texto
- [x] Validação de tamanho da linha (CNAB 400)
- [ ] Validação de registros obrigatórios
- [ ] Suporte a múltiplos layouts
- [ ] CLI para execução via terminal

## 🛠️ Tecnologias
- Python 3.10+
- Estrutura modular
- Testes com pytest (planejado)

## ▶️ Como executar

```bash
python main.py caminho/do/arquivo.txt
```

## 📂 Estrutura do Projeto

```text
CNABEngine/
├── cnabengine/        # Código-fonte principal
│   ├── core/          # Regras de validação
│   ├── layouts/       # Definições de layouts CNAB
│   └── utils/         # Funções utilitárias
├── tests/             # Testes automatizados
├── examples/          # Arquivos de exemplo
├── main.py            # Ponto de entrada da aplicação
└── README.md
```

## ⚠️ Observações

- Projeto em fase inicial de desenvolvimento
- Estrutura sujeita a mudanças
- Foco atual em validação de arquivos CNAB 400
- Ainda não há persistência em banco de dados
- Testado com Python 3.14

## 📄 Licença

Este projeto está licenciado sob a licença MIT.  
Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
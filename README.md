# 🎓 Dissertação de Mestrado — PPgCC / UFAC

<div align="center">
  <h3><em>"Aplicação de Mineração de Dados e Aprendizagem de Máquina na Detecção de Conflitos entre Políticas de Controle de Acesso"</em></h3>
  <p>
    <strong>Autor:</strong> <a href="https://github.com/ed1rac">Edkallenn Lima</a> &bull;
    <strong>Orientadora:</strong> Dra. Laura Costa Sarkis<br>
    <strong>Instituição:</strong> Programa de Pós-Graduação em Ciência da Computação (PPgCC) — Universidade Federal do Acre (UFAC)
  </p>
  <p>
    <a href="./old/dissertacao-ed-revisada.pdf"><img src="https://img.shields.io/badge/Texto_Completo-PDF_Revisado-red.svg?logo=adobeacrobatreader" alt="PDF da Dissertação"></a>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.x-blue.svg?logo=python" alt="Python"></a>
    <a href="https://scikit-learn.org/"><img src="https://img.shields.io/badge/scikit--learn-MLP_Classifier-orange.svg?logo=scikit-learn" alt="Scikit-Learn"></a>
    <a href="https://www.latex-project.org/"><img src="https://img.shields.io/badge/Documento-%C2%AALaTeX-green.svg?logo=latex" alt="LaTeX"></a>
    <a href="https://colab.research.google.com/github/ed1rac/Dissertacao-Ed/blob/master/Classifica%C3%A7%C3%A3o_Mestrado_Redes_Neurais_MLP_e_outros_Vers%C3%A3o_NOVA.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>
  </p>
</div>

---

## 📌 Resumo do Trabalho (Abstract)

As políticas de controle de acesso são componentes críticos na segurança de sistemas modernos, definindo quem pode acessar quais recursos sob quais circunstâncias. No entanto, à medida que organizações crescem e as políticas se tornam mais complexas e dinâmicas, surgem **conflitos indiretos** — situações sutis em que regras aparentemente compatíveis produzem decisões contraditórias de permissão e negação.

Esta dissertação propõe e avalia uma abordagem computacional baseada em **Mineração de Dados e Aprendizado de Máquina**, utilizando redes neurais artificiais (**Multilayer Perceptron - MLP**) e algoritmos de classificação supervisionada para automatizar a identificação, classificação e mitigação de conflitos entre políticas de controle de acesso (baseadas em padrões como XACML e RBAC).

---

## 🔬 Experimentos e Notebooks Interativos

Você pode inspecionar e reproduzir os experimentos interativamente pelo Google Colab:

| Notebook | Descrição | Executar |
| :--- | :--- | :---: |
| `Classificação_Mestrado_Redes_Neurais_MLP_e_outros_Versão_NOVA.ipynb` | Treinamento e avaliação de modelos neurais (MLP), SVM e árvores de decisão na classificação de regras | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ed1rac/Dissertacao-Ed/blob/master/Classifica%C3%A7%C3%A3o_Mestrado_Redes_Neurais_MLP_e_outros_Vers%C3%A3o_NOVA.ipynb) |
| `Abordagem conflitos indiretos.ipynb` | Pré-processamento, engenharia de atributos e análise de conflitos indiretos em políticas de acesso | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ed1rac/Dissertacao-Ed/blob/master/Abordagem%20conflitos%20indiretos.ipynb) |

---

## 📂 Estrutura do Repositório

```text
Dissertacao-Ed/
├── old/dissertacao-ed-revisada.pdf      # Texto final integral revisado da dissertação
├── old/                                 # Fontes em LaTeX (compilação completa)
├── arquivos-politicas/                  # Datasets e arquivos de políticas de controle de acesso
├── Programas/                           # Scripts Python auxiliares e rotinas de extração
├── imagens/                             # Gráficos de acurácia, matrizes de confusão e arquitetura
└── bibliografias-temp/                  # Arquivos de referências bibliográficas (.bib)
```

---

## 🛠️ Stack Tecnológica Utilizada

- **Linguagem**: Python 3 (Pandas, NumPy, Scikit-Learn, TensorFlow, Keras, PyTorch, Seaborn, Matplotlib)
- **Editor $\LaTeX$**: TeXstudio & TeX Live
- **Ambientes de Computação**: Google Colab, Jupyter Notebook, Spyder & VS Code

---

## 📖 Como Citar (BibTeX)

Se este trabalho ou dataset for útil para sua pesquisa, por favor cite:

```bibtex
@mastersthesis{lima2018conflitos,
  author       = {Edkallenn Silva Lima},
  title        = {Aplicação de Mineração de Dados e Aprendizagem de Máquina na Detecção de Conflitos entre Políticas de Controle de Acesso},
  school       = {Universidade Federal do Acre (UFAC) -- Programa de Pós-Graduação em Ciência da Computação},
  year         = {2018},
  address      = {Rio Branco, AC, Brasil},
  type         = {Dissertação de Mestrado}
}
```

---

## ☕ Apoie o Projeto (Me Pague um Café / Buy Me a Coffee)

Este projeto é desenvolvido com dedicação e carinho à disseminação do conhecimento e da tecnologia. Se ele foi útil para os seus estudos, aulas, trabalho ou produtividade diária e você quiser apoiar o desenvolvimento contínuo:

- ☕ **Buy Me a Coffee (Internacional / Cartão / QR Code)**:
  - 👉 **[https://buymeacoffee.com/edkallenn](https://buymeacoffee.com/edkallenn)**
  - [![](https://img.shields.io/badge/☕_Buy_Me_a_Coffee-Apoiar_Projeto-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/edkallenn)
  - Escaneie o QR Code abaixo com a câmera do celular para abrir diretamente:

<div align="center">
  <a href="https://buymeacoffee.com/edkallenn" target="_blank">
    <img src="./bmc_qr.png" alt="Buy Me a Coffee QR Code — Edkallenn (@ed1rac)" width="220" />
  </a>
</div>

- 🇧🇷 **PIX (Brasil — Qualquer valor, taxa zero)**:
  - **Chave PIX (E-mail)**: `edkevan@gmail.com`
  - **Titular**: Edkallenn

Muito obrigado pelo apoio! 🚀

---

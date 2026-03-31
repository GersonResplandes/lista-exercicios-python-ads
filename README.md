# Lista de Exercícios - Python (Fundamentos & Tipagem)

Repositório contendo soluções para uma lista de exercícios práticos de fundamentos de programação em Python, voltados para o curso de Análise e Desenvolvimento de Sistemas (ADS). Todos os algoritmos foram desenvolvidos utilizando boas práticas, modularidade e forte tipagem estática.

## 📁 Estrutura do Repositório

| Arquivo | Questão / Funcionalidade |
| --- | --- |
| `q1_gorjeta.py` | Calculadora de Gorjeta |
| `q2_nomes.py` | Analisador de Nomes (Contagem de caracteres) |
| `q3_idade.py` | Conversor de Idade (Para meses e dias) |
| `q4_repetidor.py` | Repetidor de Mensagens |
| `q5_par_impar.py` | Verificador de Número (Par ou Ímpar) |
| `q6_multa.py` | Calculadora de Multa de Trânsito |
| `q7_viagem.py` | Calculadora de Tarifas e Custo de Viagem |
| `q8_alistamento.py` | Analisador de Idade para Alistamento Militar |
| `q9_emprestimo.py` | Sistema de Análise e Aprovação de Empréstimo |
| `q10_imc.py` | Calculadora e Classificador de IMC |
| `q11_desconto.py` | Calculadora de Descontos por Categoria de Produto |
| `q12_data.py` | Validador Lógico de Data (Dia, Mês, Ano) |

> [!NOTE]
> **Evolução da Estrutura:** Futuramente, este repositório será reorganizado por aulas/tópicos para melhor separação dos conceitos abordados. O formato previsto será semelhante a:
> 
> ```text
> lista-exercicios-python-ads
> ├── Aula 01: Variáveis, Tipos de Dados...
> │   ├── q1_gorjeta.py
> │   ├── q2_nomes.py
> │   └── ...
> ├── Aula 02 ...
> ```

## 🚀 Tecnologias e Padrões Adotados
- **Linguagem:** Python 3+
- **Tipagem:** Uso extensivo de *Type Hints* nativos da linguagem para maior previsibilidade de tipo (`int`, `float`, `str`, `tuple`).
- **Arquitetura/Design:** Scripts modulares encapsulando a lógica nas respectivas funções e a execução central isolada no escopo estrito via `if __name__ == "__main__":`.

## ⚙️ Como Executar

Clone este repositório e execute o script das respectivas questões via CLI.

```bash
# Clone este repositório
git clone https://github.com/GersonResplandes/lista-exercicios-python-ads.git

# Acesse o diretório
cd lista-exercicios-python-ads

# Execute o exercício desejado (ex: Questão 1)
python q1_gorjeta.py
```

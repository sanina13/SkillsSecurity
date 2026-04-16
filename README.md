# SkillsSecurity

Um scanner que analisa ficheiros `.md` de skills e deteta tentativas de prompt injection antes que cheguem a um LLM.

## Porque é que isto existe

Em 15 de abril de 2026, numa talk do Google Developer Groups intitulada "Coding with AI: A Software Engineer's Perspective", Filipe Cabaço (Team Leader na Supabase) partilhou uma visão sobre o futuro da programação na era da AI que mudou a forma como eu olhava para a minha carreira.

A pergunta era simples: que projeto devo pôr no meu GitHub para ter a melhor chance de emprego? Mas a resposta honesta obrigou-me a enfrentar uma verdade desconfortável — a AI está a mudar o que significa ser programador. Escrever código está a tornar-se cada vez mais uma commodity. A AI já o faz razoavelmente bem, e vai fazê-lo melhor.

Então a pergunta certa não era "que linguagem aprendo?" mas sim **"que competências me tornam insubstituível?"**

Olhei para os dados. O gap de talento em cibersegurança passou dos 4.8 milhões de vagas globalmente em 2026. Na Europa, a diretiva NIS2 entrou em vigor e milhares de empresas estão a ser forçadas a contratar profissionais que não existem em número suficiente. Mas havia um sub-nicho que se destacava de todos os outros: **AI Security**.

Há três anos, "AI Security Engineer" mal era um título de trabalho. Hoje, o SANS Institute relata mais de 2.500 vagas ativas só para essa função. É uma área onde a AI não consegue substituir-se a si própria — proteger sistemas de AI contra ataques adversariais, data poisoning, e prompt injection requer julgamento humano, criatividade, e mentalidade de atacante.

Foi aí que decidi: em vez de construir mais um clone de Trello ou outro dashboard genérico, ia construir algo neste espaço. Algo que mostrasse competências que o mercado precisa desesperadamente e onde a escassez é estrutural.

## O que é o SkillGuard

É uma web app onde se faz upload de uma skill `.md` e o sistema analisa o conteúdo à procura de padrões de prompt injection — role overrides, system message impersonation, tentativas de exfiltração de dados, jailbreak patterns.

A ideia surgiu da observação que as skills de LLMs são essencialmente ficheiros markdown que ficam no contexto do modelo. Se alguém consegue injetar instruções maliciosas nesses ficheiros, pode sequestrar o comportamento do modelo sem que o utilizador saiba. É um vetor de ataque real, sub-explorado, e que vai crescer à medida que mais empresas adotam skills como forma de estender capacidades de LLMs.

## Como está a ser construído

Este projeto está a ser construído do zero por mim, linha a linha, com metodologia TDD (Test-Driven Development). Cada regra de deteção começa com um teste vermelho, passa a verde com o código mínimo, e só depois é refactorizada.

Não é um projeto feito com AI a gerar código por mim. É um projeto onde eu aprendo — com ajuda quando fico preso, mas com entendimento crítico de cada decisão. Porque o diferenciador no mercado de trabalho do futuro não vai ser quem copia código mais rápido. Vai ser quem compreende os sistemas suficientemente bem para os proteger.

## Estado atual

Em desenvolvimento ativo. A Fase 1 (motor de deteção) está em construção, com regras para:

- Role override attempts
- System message impersonation

Próximas fases: API REST com FastAPI, frontend React, e uma camada final de deteção semântica baseada em LLM para apanhar injeções que regras regex não conseguem detetar.

## Stack

- **Backend**: Python, FastAPI, pytest
- **Frontend**: React (em breve)
- **Testes**: pytest com cobertura de cada regra de deteção

---

*"Começa já a construir algo."*

— da conversa que iniciou este projeto, 15 de abril de 2026

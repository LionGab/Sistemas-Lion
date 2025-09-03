# /implement_agro_automation

Considerando a análise aprofundada da "Operação Safra Automatizada" e as capacidades do Claude Code, um prompt de comando eficaz para o Claude Code deve ser **extremamente detalhado, focado nos requisitos de negócio e compliance do agronegócio em Mato Grosso**, e deve alavancar as funcionalidades avançadas do Claude Code.

Aqui está um exemplo de prompt para o Claude Code, focado em um dos maiores gaps identificados: **automação de compliance fiscal e integração regional em ERPs agro**:

---

**Comando Principal para o Claude Code:**

```
/implement_agro_automation --client="Fazenda Brasil - Campo Verde/MT" --erp="TOTVS Agro Multicultivo" --focus="NFP-e & Cooperfibra Integration"
```

---

**Instruções Detalhadas para o Claude Code (como um `initial.md` ou sequência de prompts):**

"Olá Claude Code. Você é agora um **Especialista em Automação Inteligente para Agronegócio no Mato Grosso**, com profundo conhecimento em compliance fiscal brasileiro e integrações regionais. Sua missão é **desenvolver e implementar um módulo de automação no ERP TOTVS Agro Multicultivo** para a 'Fazenda Brasil' em Campo Verde/MT.

**Objetivo:**
**Automatizar 90% do processo de emissão da Nota Fiscal do Produtor Eletrônica (NFP-e)** para produtores rurais pessoa física em Mato Grosso, conforme a obrigatoriedade desde Março/2022. Além disso, garantir a **integração automática de romaneios de colheita e liquidação financeira com a Cooperfibra**, uma cooperativa local chave.

**Contexto Atual do Cliente:**
*   **ERP:** TOTVS Agro Multicultivo (Protheus Agro).
*   **Localização:** Campo Verde, Mato Grosso.
*   **Problema:** Atualmente, a NFP-e é gerada e enviada manualmente, e os dados de recebimento da Cooperfibra são inseridos manualmente no ERP. Isso causa atrasos, erros e potencial risco de multas fiscais.

**Requisitos e Fluxo de Trabalho (Utilizando as capacidades do Claude Code):**

1.  **Regras Globais (`claw.md`):**
    *   Atualize ou crie um arquivo `claw.md` na raiz do projeto, definindo as **melhores práticas de compliance fiscal para MT (NFP-e, SPED Fiscal, FUNRURAL)**.
    *   Inclua diretrizes para **segurança de dados sensíveis** do cliente (LGPD).

2.  **Comando Slash Personalizado para NFP-e (`/emitirNFPeAgro`):**
    *   Desenvolva um comando `/.claude/commands/emitirNFPeAgro.md` que automatize a geração e envio da NFP-e via SEFAZ-MT.
    *   Este comando deve aceitar como parâmetros o número do romaneio da Cooperfibra e dados básicos do produtor/talhão.
    *   O comando deve orquestrar a interação com as APIs da SEFAZ-MT e o ERP TOTVS para extrair e inserir dados.

3.  **Sub-Agente de Validação de Compliance (`/validation_compliance`):**
    *   Crie um sub-agente especializado `/.claude/agents/validation_compliance.md` com um `system prompt` focado em **auditoria fiscal de agro**.
    *   Após a geração da NFP-e pelo agente principal, o sub-agente deve ser invocado para realizar uma validação automática dos dados gerados com as regras do SPED Fiscal e do FUNRURAL.
    *   Ele deve reportar quaisquer inconsistências ou potenciais erros de conformidade ao agente principal em um arquivo Markdown de saída.

4.  **Integração com Cooperfibra (Usando MCP):**
    *   Utilize o **Serena MCP Server** para auxiliar na compreensão semântica da documentação das APIs da Cooperfibra.
    *   Implemente a integração para recebimento com classificação automática, controle por produtor/talhão, liquidação financeira e notas de depósito, conforme a documentação da Cooperfibra.

5.  **Robustez e Segurança:**
    *   O código deve ser **`production-ready`**, com foco em **segurança** e **escalabilidade**.
    *   Preveja **capacidade offline robusta** para o módulo, devido à conectividade rural limitada em 64% das propriedades brasileiras.
    *   Para as fases de teste e deploy automático, utilize o **YOLO mode** dentro de um **dev container** isolado, protegendo o ambiente host.

6.  **Saída Desejada (Deliverables):**
    *   Um conjunto de arquivos de código-fonte (preferencialmente Python/FastAPI ou Next.js, para prototipagem rápida).
    *   Testes unitários abrangentes (TDD).
    *   Documentação técnica automática para o módulo.
    *   Um relatório sumarizando as decisões de arquitetura e os pontos de compliance abordados.

**Dica Final:**
*   **Ultrathink:** Use a palavra-chave `ultrathink` no prompt inicial para garantir que o Claude Code dedique mais tokens para planejar e pensar criticamente sobre o problema e a solução antes de gerar o código.
*   **Checkpointing:** Crie checkpoints verificáveis em cada fase do desenvolvimento para que possamos monitorar o progresso e garantir a correção sem a necessidade de uma revisão linha a linha.

---

Este prompt é um exemplo de como aproveitar as capacidades do Claude Code para resolver problemas complexos e de alto valor no agronegócio, alinhado com a estratégia de "Operação Safra Automatizada". Ele direciona o Claude Code a atuar como um **arquiteto de sistemas assistido por IA**, focando na solução de problemas, não apenas na codificação.
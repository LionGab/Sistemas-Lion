# /implement_agro_automation

## Purpose
Implement intelligent automation for specific agribusiness processes using Claude Code + TOTVS Agro integration.

## Parameters
- `process_type`: (required) Type of automation [nfpe, sped, estoque, safra, compliance]
- `fazenda_id`: (required) Farm identifier for context
- `priority`: (optional) Implementation priority [urgent, high, medium, low] (default: high)
- `integration_scope`: (optional) Integration scope [totvs_only, full_stack, compliance_only] (default: full_stack)

## Usage Examples
```
/implement_agro_automation process_type=nfpe fazenda_id=fazenda_brasil priority=urgent
/implement_agro_automation process_type=estoque fazenda_id=cooperfibra_001 integration_scope=totvs_only
/implement_agro_automation process_type=safra fazenda_id=fazenda_brasil priority=high
```

## Sub-agent Workflow
1. **Analysis Sub-agent**: Analyze current process and integration points
2. **Architecture Sub-agent**: Design technical implementation approach  
3. **Compliance Sub-agent**: Ensure fiscal/regulatory compliance
4. **Implementation Sub-agent**: Execute code generation and integration
5. **Validation Sub-agent**: Test and validate automation end-to-end

## Expected Deliverables
- Technical implementation plan with ROI projections
- Working automation code (Python/FastAPI)
- TOTVS Agro integration configured
- Compliance validation reports
- Documentation and team training materials
- Monitoring and alerting setup

## Success Criteria
- ✅ Automation reduces manual work by 70-90%
- ✅ 100% compliance with SEFAZ-MT requirements
- ✅ Zero errors in fiscal document generation
- ✅ Team can operate autonomously after training
- ✅ ROI validated within first 30 days
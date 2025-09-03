# /validateNFPe Command
## Automated NFP-e Validation Against SEFAZ-MT Requirements

---

## COMMAND METADATA

**Name**: validateNFPe
**Description**: Validates NFP-e data against SEFAZ-MT v4.0 requirements
**Category**: Fiscal Compliance
**Priority**: Critical
**Execution Time**: ~2-5 seconds

---

## USAGE

```bash
/validateNFPe [file_path|json_data] [--options]
```

### Parameters
- `file_path`: Path to NFP-e XML or JSON file
- `json_data`: Inline JSON data for validation
- `--strict`: Enable strict mode (fail on warnings)
- `--fix`: Attempt automatic fixes for common issues
- `--report`: Generate detailed compliance report

### Examples
```bash
# Validate XML file
/validateNFPe /fiscal/nfpe/2024/NFe43240001234567.xml

# Validate with auto-fix
/validateNFPe /fiscal/pending/draft_nfpe.json --fix

# Generate compliance report
/validateNFPe /fiscal/batch/*.xml --report
```

---

## WORKFLOW

```python
async def execute_validateNFPe(params):
    """
    Main workflow for NFP-e validation command
    """
    # Step 1: Parse input
    data = await parse_nfpe_input(params)
    
    # Step 2: Invoke FiscalComplianceAgent
    agent = FiscalComplianceAgent()
    
    # Step 3: Schema validation
    schema_result = await agent.validate_schema(
        data, 
        schema="SEFAZ_MT_v4.0"
    )
    
    # Step 4: Business rules validation
    rules_result = await agent.validate_business_rules(data)
    
    # Step 5: Fix issues if requested
    if params.get("fix"):
        data = await agent.auto_fix_issues(data, schema_result)
    
    # Step 6: Generate report
    report = await generate_validation_report(
        data, 
        schema_result, 
        rules_result
    )
    
    # Step 7: Return results
    return ValidationResult(
        status=report.status,
        data=data if params.get("fix") else None,
        report=report if params.get("report") else report.summary
    )
```

---

## VALIDATION CHECKLIST

### Schema Validation (XSD)
- [ ] XML structure compliance
- [ ] Required fields presence
- [ ] Data types correctness
- [ ] Field length constraints
- [ ] Enumeration values
- [ ] Pattern matching (regex)

### Business Rules
- [ ] CNPJ/CPF validity
- [ ] NCM code existence
- [ ] CFOP appropriateness
- [ ] Tax calculations accuracy
- [ ] Date sequence logic
- [ ] Value consistency

### SEFAZ-MT Specific
- [ ] MT inscription validity
- [ ] Regional tax rules
- [ ] Contingency requirements
- [ ] Digital signature presence
- [ ] Certificate validity

---

## ERROR HANDLING

### Common Validation Errors
```python
VALIDATION_ERRORS = {
    "SCHEMA_001": {
        "description": "Missing required field",
        "fix": "Add field with default value",
        "severity": "ERROR"
    },
    "SCHEMA_002": {
        "description": "Invalid data type",
        "fix": "Convert to correct type",
        "severity": "ERROR"
    },
    "BUSINESS_001": {
        "description": "Invalid CNPJ checksum",
        "fix": "Recalculate checksum digits",
        "severity": "ERROR"
    },
    "BUSINESS_002": {
        "description": "ICMS calculation mismatch",
        "fix": "Recalculate based on NCM",
        "severity": "WARNING"
    },
    "SEFAZ_001": {
        "description": "Expired digital certificate",
        "fix": "Request certificate renewal",
        "severity": "CRITICAL"
    }
}
```

### Auto-Fix Logic
```python
async def auto_fix_issue(data, error):
    """
    Attempts to automatically fix common validation issues
    """
    if error.code == "SCHEMA_001":
        # Add missing field with default
        data[error.field] = get_default_value(error.field)
        
    elif error.code == "BUSINESS_001":
        # Fix CNPJ checksum
        data["cnpj"] = fix_cnpj_checksum(data["cnpj"])
        
    elif error.code == "BUSINESS_002":
        # Recalculate taxes
        data["icms"] = calculate_icms(
            data["base_calculo"], 
            data["ncm"]
        )
    
    return data
```

---

## OUTPUT FORMAT

### Summary Mode
```markdown
# NFP-e Validation Summary
**Status**: ❌ FAILED (3 errors, 2 warnings)
**File**: NFe43240001234567.xml
**Timestamp**: 2024-01-15T10:30:45Z

## Critical Issues
- 🔴 Missing required field: `emit.IE`
- 🔴 Invalid CNPJ format: `12.345.678/0001-90`
- 🔴 ICMS calculation error: Expected 1,234.56, Got 1,234.57

## Warnings
- 🟡 NCM code deprecated, consider updating
- 🟡 Optional field recommended: `infAdic`

**Action Required**: Fix critical issues before transmission
```

### Detailed Report Mode
```markdown
# NFP-e Compliance Report
**Generated**: 2024-01-15T10:30:45Z
**Validator**: SEFAZ-MT v4.0

## Document Information
- Number: 001234
- Series: 1
- Emission: 2024-01-15
- Emitter: FAZENDA BRASIL LTDA

## Validation Results

### ✅ PASSED (47 checks)
- XML Schema: Valid
- Digital Signature: Present and valid
- Certificate: Valid until 2024-12-31
- [... 44 more ...]

### ❌ FAILED (3 checks)
1. **Field**: emit.IE
   - **Error**: Required field missing
   - **Impact**: SEFAZ rejection guaranteed
   - **Fix**: Add MT state inscription number

2. **Field**: emit.CNPJ
   - **Error**: Invalid format
   - **Current**: "12.345.678/0001-90"
   - **Expected**: "12345678000190"
   - **Fix**: Remove formatting characters

3. **Field**: ICMS.vICMS
   - **Error**: Calculation mismatch
   - **Calculated**: 1,234.56
   - **Provided**: 1,234.57
   - **Fix**: Recalculate using correct rate

### 🟡 WARNINGS (2 items)
[...]

## Recommendations
1. Update to latest NCM table (2024 version)
2. Include additional information for traceability
3. Consider implementing automated validation before generation

## Compliance Score: 94/100
```

---

## INTEGRATION POINTS

### Sequential Thinking MCP
```python
# Use for complex validation chains
async def complex_validation_chain(data):
    async with sequential_thinking.think() as thinker:
        # Step 1: Analyze document structure
        structure = await thinker.analyze_structure(data)
        
        # Step 2: Validate dependencies
        deps = await thinker.validate_dependencies(structure)
        
        # Step 3: Check cross-references
        refs = await thinker.check_references(deps)
        
        # Step 4: Final validation
        result = await thinker.final_validation(refs)
    
    return result
```

### File System Operations
```python
# Batch validation support
async def validate_batch(pattern):
    files = await filesystem.glob(pattern)
    results = []
    
    for file in files:
        result = await validate_single(file)
        results.append(result)
    
    return aggregate_results(results)
```

---

## PERFORMANCE OPTIMIZATION

### Caching Strategy
- Cache XSD schemas (24 hours)
- Cache NCM tables (7 days)
- Cache validation results (1 hour)
- Cache CNPJ validations (30 days)

### Parallel Processing
```python
# Validate multiple documents in parallel
async def parallel_validate(documents):
    tasks = [validate_document(doc) for doc in documents]
    results = await asyncio.gather(*tasks)
    return results
```

---

## MONITORING & METRICS

### Command Metrics
```python
metrics = {
    "execution_count": Counter("Total executions"),
    "validation_time": Histogram("Validation duration"),
    "error_rate": Gauge("Validation error rate"),
    "auto_fix_success": Counter("Successful auto-fixes")
}
```

### Success Criteria
- Execution time < 5 seconds
- Auto-fix success rate > 80%
- False positive rate < 1%
- Memory usage < 100MB

---

*This command provides comprehensive NFP-e validation with automatic fixing capabilities, ensuring compliance before SEFAZ transmission.*
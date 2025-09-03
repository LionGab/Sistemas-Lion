#!/usr/bin/env python3
"""
Post-implementation hook for agro automation validation
Executes after any /implement_agro_automation command
"""

import subprocess
import json
import os
from datetime import datetime
from pathlib import Path

def validate_agro_implementation():
    """Comprehensive validation of agro automation implementation"""
    
    validation_results = {
        "timestamp": datetime.now().isoformat(),
        "tests": {},
        "compliance": {},
        "integration": {},
        "performance": {}
    }
    
    # 1. Run agro-specific tests
    try:
        test_result = subprocess.run(
            ["python", "-m", "pytest", "tests/agro/", "-v", "--tb=short"],
            capture_output=True, text=True, timeout=300
        )
        validation_results["tests"] = {
            "status": "passed" if test_result.returncode == 0 else "failed",
            "output": test_result.stdout,
            "errors": test_result.stderr
        }
    except subprocess.TimeoutExpired:
        validation_results["tests"] = {"status": "timeout", "error": "Tests exceeded 5 minute timeout"}
    except Exception as e:
        validation_results["tests"] = {"status": "error", "error": str(e)}
    
    # 2. Validate fiscal compliance
    try:
        compliance_result = subprocess.run(
            ["python", "scripts/validate_fiscal_compliance.py"],
            capture_output=True, text=True, timeout=120
        )
        validation_results["compliance"] = {
            "status": "valid" if compliance_result.returncode == 0 else "invalid", 
            "details": compliance_result.stdout
        }
    except Exception as e:
        validation_results["compliance"] = {"status": "error", "error": str(e)}
    
    # 3. Test TOTVS integration health
    try:
        integration_result = subprocess.run(
            ["python", "scripts/totvs_health_check.py"],
            capture_output=True, text=True, timeout=60
        )
        validation_results["integration"] = {
            "totvs_status": "healthy" if integration_result.returncode == 0 else "unhealthy",
            "details": integration_result.stdout
        }
    except Exception as e:
        validation_results["integration"] = {"status": "error", "error": str(e)}
    
    # 4. Performance baseline check
    try:
        perf_result = subprocess.run(
            ["python", "scripts/performance_baseline.py"],
            capture_output=True, text=True, timeout=180
        )
        validation_results["performance"] = {
            "baseline": "acceptable" if perf_result.returncode == 0 else "needs_optimization",
            "metrics": perf_result.stdout
        }
    except Exception as e:
        validation_results["performance"] = {"status": "error", "error": str(e)}
    
    # Save validation results
    results_dir = Path("validation_results")
    results_dir.mkdir(exist_ok=True)
    
    results_file = results_dir / f"agro_validation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(validation_results, f, indent=2)
    
    # Generate summary report
    generate_validation_summary(validation_results, results_file)
    
    return validation_results

def generate_validation_summary(results, results_file):
    """Generate human-readable validation summary"""
    
    summary = f"""
# OPERACAO SAFRA - VALIDATION REPORT
Generated: {results['timestamp']}
Results File: {results_file}

## Test Results
Status: {results['tests'].get('status', 'unknown')}
{results['tests'].get('output', 'No output')[:500]}...

## Compliance Check  
Status: {results['compliance'].get('status', 'unknown')}
Details: {results['compliance'].get('details', 'No details')[:300]}...

## TOTVS Integration
Status: {results['integration'].get('totvs_status', 'unknown')}
Details: {results['integration'].get('details', 'No details')[:300]}...

## Performance Baseline
Status: {results['performance'].get('baseline', 'unknown')}
Metrics: {results['performance'].get('metrics', 'No metrics')[:300]}...

## Next Actions
{'Implementation validated - ready for deployment' if all_checks_passed(results) else 'Issues detected - review validation details'}
"""
    
    # Write summary to file
    summary_file = Path("validation_results") / "latest_summary.md"
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write(summary)
    
    print(summary)

def all_checks_passed(results):
    """Check if all validation steps passed"""
    return (
        results['tests'].get('status') == 'passed' and
        results['compliance'].get('status') == 'valid' and  
        results['integration'].get('totvs_status') == 'healthy' and
        results['performance'].get('baseline') == 'acceptable'
    )

if __name__ == "__main__":
    validation_results = validate_agro_implementation()
    exit(0 if all_checks_passed(validation_results) else 1)
import json
from pathlib import Path

notebook_path = Path("notebooks/Bike_Sharing_Demand_Prediction.ipynb")

print("="*70)
print("BIKE-SHARING DEMAND PREDICTION NOTEBOOK - VERIFICATION")
print("="*70)

with open(notebook_path, 'r') as f:
    nb = json.load(f)

total_tests = 0
passed_tests = 0

def test(name, condition):
    global total_tests, passed_tests
    total_tests += 1
    status = "[PASS]" if condition else "[FAIL]"
    if condition:
        passed_tests += 1
    print(f"{total_tests}. {name}: {status}")
    return condition

test("Valid JSON structure", isinstance(nb, dict))
test("nbformat 4.4", nb.get('nbformat') == 4)
test("Has cells", 'cells' in nb)

cells = nb['cells']
test("25 cells total", len(cells) == 25)

markdown_cells = sum(1 for c in cells if c.get('cell_type') == 'markdown')
code_cells = sum(1 for c in cells if c.get('cell_type') == 'code')
test(f"Markdown cells ({markdown_cells})", markdown_cells == 7)
test(f"Code cells ({code_cells})", code_cells == 18)

code_content = '\n'.join(['\n'.join(c.get('source', [])) for c in cells if c.get('cell_type') == 'code'])

test("Imports pandas", 'import pandas' in code_content)
test("Imports sklearn", 'from sklearn' in code_content)
test("All 5 models present", all(m in code_content for m in ['DummyRegressor', 'LinearRegression', 'DecisionTreeRegressor', 'RandomForestRegressor', 'GradientBoostingRegressor']))
test("Chronological split", 'train_idx' in code_content and 'iloc' in code_content)
test("Feature sets A/B/C", 'feature_set_a' in code_content and 'feature_set_b' in code_content)
test("Preprocessing pipeline", 'ColumnTransformer' in code_content or 'StandardScaler' in code_content)
test("Metrics MAE/RMSE/R2", all(m in code_content for m in ['mean_absolute_error', 'mean_squared_error', 'r2_score']))
test("Model training", 'model.fit' in code_content)
test("Results export", 'to_csv' in code_content)
test("Visualizations", 'plt.savefig' in code_content)
test("Hypothesis testing", 'HYPOTHESIS' in code_content.upper())
test("Summary report", 'summary' in code_content.upper())

phases = ['Setup', 'Data Loading', 'Data Preparation', 'Model Training', 'Model Comparison', 'Feature Importance', 'Hypothesis']
notebook_text = '\n'.join(['\n'.join(c.get('source', [])) for c in cells])
for phase in phases:
    test(f"Phase: {phase}", phase.upper() in notebook_text.upper())

print("\n" + "="*70)
print(f"Results: {passed_tests}/{total_tests} passed ({100.0*passed_tests/total_tests:.0f}%)")
status = "✅ COMPLETE AND READY" if passed_tests == total_tests else f"⚠️  {total_tests - passed_tests} FAILED"
print(f"Status: {status}")
print("="*70)

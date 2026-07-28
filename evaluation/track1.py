import json
import argparse
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

parser = argparse.ArgumentParser()
parser.add_argument("--system", type=str)
parser.add_argument("--reference", type=str)
args = parser.parse_args()

y_pred = [json.loads(line.strip())['Value'] for line in open(args.system, 'r', encoding='utf-8') if
          line.strip()]
y_true = [json.loads(line.strip())['Value'] for line in open(args.reference, 'r', encoding='utf-8') if
          line.strip()]

acc = accuracy_score(y_true, y_pred)
p = precision_score(y_true, y_pred, average="weighted")
r = recall_score(y_true, y_pred, average="weighted")
f1 = f1_score(y_true, y_pred, average="weighted")

print(f"准确率: {acc:.4f}")
print(f"精确率P: {p:.4f}")
print(f"召回率R: {r:.4f}")
print(f"F1: {f1:.4f}")

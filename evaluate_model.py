import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 읽기 (파일명은 네가 저장한 경로로 바꿔줘)
df = pd.read_csv('final_result_log.csv')  # 예: 'pruning_results.csv'

# 컬럼명 확인 (필요 시 수정)
print(df.columns)
df = df.sort_values('prune_ratio')
# 프루닝 비율과 mAP 가져오기
prune_ratios = df['prune_ratio']
final_mAPs = df['final_mAP']

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(prune_ratios, final_mAPs, marker='o', linestyle='-', color='royalblue', label='Final mAP')
plt.xlabel('Prune Ratio')
plt.ylabel('Final mAP')
plt.title('Final mAP')
plt.grid(True)
plt.xticks(prune_ratios)
plt.legend()
plt.tight_layout()
plt.savefig('retinanet_pruning_mAP.png', dpi=300)  # 해상도 300으로 저장
plt.show()


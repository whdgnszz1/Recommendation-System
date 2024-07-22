from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz  # 결정트리 시각화
from subprocess import check_call

iris = load_iris()  # iris 데이터 로드
x = iris.data[:, 2:]  # 꽃잎의 길이, 너비 변수를 사용하겠다.
y = iris.target

# decision tree 모형 인스턴스 생성 및 하이퍼 파라미터를 설정
# 사이킷런에서 제공하는 모델 => 모형 인스턴스 생성 => 인스턴스.fit() 반복
tree_model = DecisionTreeClassifier(max_depth=3)
tree_model.fit(x, y)

export_graphviz(
    tree_model, # 학습한 모형
    feature_names=iris.feature_names[2:], # 사용한 변수 이름
    class_names=iris.target_names, # 예측한 타겟 클래스 이름
    rounded=True,
    filled=True,
    out_file='./iris_tree_model.dot'
)

# 예측한 모형을 png로 바꿔서 시각화
check_call(['dot', '-Tpng', 'iris_tree_model.dot', '-o', 'OutputFile.png'])
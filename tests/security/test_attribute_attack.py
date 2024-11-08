   
def test_attribute_attack_score():
    from holistic.datasets import load_dataset
    from holistic.security.metrics import attribute_attack_score

    dataset = load_dataset('adult')
    train_test = dataset.train_test_split(0.2, random_state=42)
    train = train_test['train']
    test = train_test['test']

    score = attribute_attack_score(train['X'], test['X'], train['y'], test['y'], attribute_attack='age')
    assert score >= 0.0
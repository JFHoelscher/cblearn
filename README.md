# cblearn
## Comparison-based Machine Learning in Python
:warning: **cblearn** is **work in progress**. The API can change and bugs appear. Please help us by posting an [issue]( https://github.com/dekuenstle/cblearn/issues/new) :construction:
 
[![Unit tests](https://github.com/dekuenstle/cblearn/workflows/Python%20package/badge.svg)](https://github.com/dekuenstle/cblearn/actions)
[![Test Coverage](https://codecov.io/gh/dekuenstle/cblearn/branch/master/graph/badge.svg?token=P9JRT6OK6O)](https://codecov.io/gh/dekuenstle/cblearn)
[![Documentation](https://readthedocs.org/projects/cblearn/badge/?version=latest)](https://cblearn.readthedocs.io/en/latest/?badge=latest)

Comparison-based Learning are the Machine Learning algorithms to use, when training data
are ordinal comparisons instead of Euclidean points. 
Triplet comparisons can be gathered e.g. from human studies with Query like 
"Which of the following bands is most similar to Queen?".

This library provides an easy to use interface to comparison-based learning algorithms.
It plays hand-in-hand with scikit-learn:

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score

from cblearn.datasets import make_random_triplets
from cblearn.embedding import SOE
from cblearn.metrics import QueryScorer

X = load_iris().data
triplets, responses = make_random_triplets(X, size=1000)

estimator = SOE(n_components=2)
scores = cross_val_score(estimator, triplets, responses, scoring=QueryScorer, cv=5)
print(f"The 5-fold CV triplet error is {sum(scores) / len(scores)}.")

embedding = estimator.fit_transform(triplets, responses)
print(f"The embedding has shape {embedding.shape}.")
```

Please try the [Examples](https://cblearn.readthedocs.io/en/latest/generated_examples/index.html).

## Getting Started

cblearn required Python 3.7 or newer. The easiest way to install is using `pip`:

```
pip install https://github.com/dekuenstle/cblearn.git
```
Find more details in the [installation instructions](https://cblearn.readthedocs.io/en/latest/install.html).


In the [User Guide](https://cblearn.readthedocs.io/en/latest/user_guide/index.html) you find a detailed introduction.

## Features

### Datasets

*cblearn* provides utility methods to simplify the loading and conversion
of your comparison datasets. In addition, there are 
functions that download and load multiple real world comparisons.

| Dataset  | Query | #Object | #Response | #Triplet |
| --- | --- | ---:| ---:| ---:|
| Vogue Cover | Odd-out Triplet | 60 | 1,107 | 2,214 | 
| Nature Scene | Odd-out Triplet | 120 | 3,355 | 6,710 | 
| Car | Most-Central Triplet | 60 | 7,097 | 14,194 | 
| Material | Standard Triplet | 100 | 104,692 |104,692 | 
| Food | Standard Triplet | 100 | 190,376 |190,376 | 
| Musician | Standard Triplet | 413 | 224,792 |224,792 | 
| Things Image Testset | Odd-out Triplet | 1,854 | 146,012 | 292,024 | 
| ImageNet Images v0.1 | Rank 2 from 8 | 1,000 | 25,273 | 328,549 | 
| ImageNet Images v0.2 | Rank 2 from 8 | 50,000 | 384,277 | 5M | 


### Embedding Algorithms

| Algorithm                   | Default | Pytorch (GPU) | Reference Wrapper |
| --------------------------- |  :---:  | :-----------: | :---------------: |
| Crowd Kernel Learning (CKL) | X       | X             |                   |
| FORTE                       |         | X             |                   |
| GNMDS                       | X       | X             |                   |
| Maximum-Likelihood Difference Scaling (MLDS) | X |              | [MLDS (R)](https://cran.r-project.org/web/packages/MLDS/index.html)|
| Soft Ordinal Embedding (SOE) | X      | X             | [loe (R)](https://cran.r-project.org/web/packages/loe/index.html) |
| Stochastic Triplet Embedding (STE/t-STE) | X       | X  |   |

## Contribute

We are happy about your contributions.
Please see our [Contributor Guide](https://cblearn.readthedocs.io/en/latest/contributor_guide/index.html). 

## License
*cblearn* was initiated by current and former members of the [Theory of Machine Learning group](http://www.tml.cs.uni-tuebingen.de/index.php) of Prof. Dr. Ulrike von Luxburg at the University of Tübingen.
The main development is realised by [David-Elias Künstle](http://www.tml.cs.uni-tuebingen.de/team/kuenstle/index.php).

This library is free to use under the [MIT License](https://github.com/dekuenstle/cblearn/blob/master/LICENSE) conditions.

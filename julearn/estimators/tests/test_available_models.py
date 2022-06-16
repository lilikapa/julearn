# Authors: Federico Raimondo <f.raimondo@fz-juelich.de>
#          Sami Hamdan <s.hamdan@fz-juelich.de>
#          Shammi More <s.more@fz-juelich.de>
# License: AGPL

import pytest
from julearn.estimators import register_model, reset_models, get_model
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor


def test_register_model():
    register_model("dt",
                   binary_cls=DecisionTreeClassifier,
                   multiclass_cls=DecisionTreeClassifier,
                   regression_cls=DecisionTreeRegressor
                   )
    binary = get_model("dt", "binary_classification")
    multiclass = get_model("dt", "multiclass_classification")
    regression = get_model("dt", "regression")

    assert isinstance(binary, DecisionTreeClassifier)
    assert isinstance(multiclass, DecisionTreeClassifier)
    assert isinstance(regression, DecisionTreeRegressor)
    reset_models()

    with pytest.raises(ValueError, match="The specified model "):
        binary = get_model("dt", "binary_classification")

from dos_plugin_ml import risk_advisor


def test_advisor_is_restriction_only_and_bounded():
    assert risk_advisor({}, ["known_bad_actor"]) == "malicious"
    assert risk_advisor({}, ["capability_probing"]) == "suspicious"
    assert risk_advisor({}, []) is None  # cannot invent a verdict

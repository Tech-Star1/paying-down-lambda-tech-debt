from render_handler import title_for, lambda_handler


def test_title_for_formats():
    assert title_for("monthly_summary") == "Monthly Summary"
    assert title_for("pci_audit") == "Pci Audit"


def test_lambda_handler_title():
    resp = lambda_handler({"report_type": "quarterly_close"}, None)
    assert resp["statusCode"] == 200
    assert resp["body"]["title"] == "Quarterly Close"

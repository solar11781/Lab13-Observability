from __future__ import annotations

import time

from .incidents import STATE

CORPUS = {
    # 🔐 Security & PII
    "pii": ["Never expose sensitive data such as account numbers, credit cards, or CCCD. Always redact sensitive information in logs and responses."],
    "fraud": ["If fraud is suspected, immediately freeze the account and contact the bank hotline for investigation."],
    "password": ["Banking systems will never ask for your password. Do not share your credentials with anyone."],

    # 💰 Accounts
    "balance": ["Customers can check account balance via mobile app, ATM, or internet banking."],
    "account": ["A bank account allows deposits, withdrawals, and secure storage of funds."],
    "minimum balance": ["Minimum balance requirements depend on account type and bank policy."],

    # 💸 Transfers
    "transfer": ["Funds can be transferred instantly within the same bank or via interbank systems depending on service availability."],
    "limit": ["Daily transfer limits are set based on account type and security level."],
    "international": ["International transfers may take 1-3 business days and include additional fees."],

    # 💳 Cards
    "credit card": ["Credit cards allow borrowing up to a limit and must be repaid monthly to avoid interest."],
    "debit card": ["Debit cards deduct money directly from your bank account."],
    "lost card": ["Lost cards must be blocked immediately via mobile app or hotline."],

    # 🏦 Loans
    "loan": ["Loans require repayment with interest over a defined tenure."],
    "interest": ["Interest rates vary based on loan type, tenure, and customer profile."],
    "emi": ["EMI is a fixed monthly payment for loan repayment."],

    # 📊 Transactions & Summary
    "transaction": ["Transaction history shows all account activities including deposits and withdrawals."],
    "summary": ["Account summary includes balance, recent transactions, and financial activity overview."],

    # ⚙️ Operations
    "kyc": ["KYC requires identity verification using documents such as CCCD or passport."],
    "otp": ["OTP is a one-time password used for secure authentication."],
    "support": ["Customers can contact support via hotline, app chat, or branch visit."],

    # 📈 Monitoring (keep original lab intent)
    "monitoring": ["Metrics detect incidents, traces localize them, logs explain root cause."],
    "policy": ["Do not expose PII in logs. Use sanitized summaries only."],
}


def retrieve(message: str) -> list[str]:
    if STATE["tool_fail"]:
        raise RuntimeError("Vector store timeout")
    if STATE["rag_slow"]:
        time.sleep(2.5)
    lowered = message.lower()
    for key, docs in CORPUS.items():
        if key in lowered:
            return docs
    return ["No domain document matched. Use general fallback answer."]

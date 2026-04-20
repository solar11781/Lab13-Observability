# Mock Debug Q&A

## Q1. Nếu thiếu `x-request-id` thì debug như thế nào?

**Short Answer:**
Kiểm tra middleware có inject correlation ID và log schema có bind field này hay không.

**Deep Dive:**
- Step 1: Gửi request mới đến API
- Step 2: Kiểm tra response header có `x-request-id`
- Step 3: Kiểm tra logs có field này không
- Step 4: Nếu thiếu → middleware chưa set hoặc logging chưa bind

**Where to check:**
- Logs: `data/logs.jsonl`
- Code: `app/middleware.py`
- Schema: `config/logging_schema.json`

---

## Q2. Làm sao phát hiện latency tăng đột biến?

**Short Answer:**
Dựa vào p95 latency trên dashboard và so sánh với SLO.

**Deep Dive:**
- Step 1: Xem panel latency (p95)
- Step 2: So sánh với threshold trong `slo.yaml`
- Step 3: Nếu vượt → kiểm tra alert
- Step 4: Trace các request chậm để tìm bottleneck

**Where to check:**
- Metrics: `app/metrics.py`
- Dashboard panel latency
- Config: `config/slo.yaml`

---

## Q3. Khi error rate tăng, bạn tìm root cause như thế nào?

**Short Answer:**
Đi từ dashboard → trace → log để xác định lỗi cụ thể.

**Deep Dive:**
- Step 1: Xem panel error rate
- Step 2: Xác định endpoint hoặc feature lỗi nhiều
- Step 3: Lấy `x-request-id`
- Step 4: Truy vết trong tracing system
- Step 5: Xem log chi tiết để tìm nguyên nhân

**Where to check:**
- Dashboard
- Traces (Langfuse)
- Logs: `data/logs.jsonl`

---

## Q4. PII được bảo vệ như thế nào trong logs?

**Short Answer:**
PII được scrub trước khi ghi log bằng các helper functions.

**Deep Dive:**
- Step 1: Input chứa email/phone
- Step 2: Logging pipeline gọi scrubber
- Step 3: Dữ liệu được mask trước khi log
- Step 4: Validate bằng script

**Where to check:**
- Code: `app/pii.py`, `app/logging_config.py`
- Script: `scripts/validate_logs.py`
- Logs: `data/logs.jsonl`

---

## Q5. Làm sao kiểm tra alert hoạt động đúng?

**Short Answer:**
Inject incident và verify alert trigger theo rule.

**Deep Dive:**
- Step 1: Chạy script inject incident
- Step 2: Tạo error hoặc latency spike
- Step 3: Kiểm tra điều kiện trong `alert_rules.yaml`
- Step 4: Xác nhận alert được kích hoạt

**Where to check:**
- Config: `config/alert_rules.yaml`
- Metrics dashboard
- Logs: xác nhận spike

---

## Q6. Làm sao xác định request nào gây lỗi cụ thể?

**Short Answer:**
Dùng `x-request-id` để truy vết từ dashboard → trace → log.

**Deep Dive:**
- Step 1: Identify request lỗi từ dashboard
- Step 2: Lấy `x-request-id`
- Step 3: Tra cứu trace tương ứng
- Step 4: Xem log chi tiết của request đó

**Where to check:**
- Logs: `data/logs.jsonl`
- Tracing system
- Dashboard

---

## Q7. Làm sao verify logging đúng schema?

**Short Answer:**
Dùng script validate để check logs theo schema định nghĩa.

**Deep Dive:**
- Step 1: Generate logs bằng load test
- Step 2: Chạy validate script
- Step 3: Kiểm tra lỗi schema nếu có
- Step 4: Fix logging config nếu fail

**Where to check:**
- Script: `scripts/validate_logs.py`
- Schema: `config/logging_schema.json`
- Logs: `data/logs.jsonl`

---

## Q8. Khi tracing không hiển thị, bạn debug thế nào?

**Short Answer:**
Kiểm tra decorator tracing và config kết nối.

**Deep Dive:**
- Step 1: Verify function có dùng decorator observe
- Step 2: Kiểm tra config Langfuse
- Step 3: Gửi request mới
- Step 4: Kiểm tra trace xuất hiện

**Where to check:**
- Code: `app/tracing.py`, `app/agent.py`
- Tracing dashboard (Langfuse)

---

## Q9. Làm sao biết hệ thống có vi phạm SLO?

**Short Answer:**
So sánh metrics thực tế với SLO định nghĩa.

**Deep Dive:**
- Step 1: Lấy metrics (latency, error rate)
- Step 2: So sánh với `slo.yaml`
- Step 3: Nếu vượt threshold → SLO violation
- Step 4: Kiểm tra alert liên quan

**Where to check:**
- Config: `config/slo.yaml`
- Dashboard panels
- Metrics data

---

## Q10. Khi inject incident, hệ thống phản ứng như thế nào?

**Short Answer:**
Metrics thay đổi, dashboard phản ánh và alert được trigger.

**Deep Dive:**
- Step 1: Chạy inject incident
- Step 2: Quan sát error/latency tăng
- Step 3: Dashboard cập nhật theo thời gian
- Step 4: Alert được kích hoạt

**Where to check:**
- Script: `scripts/inject_incident.py`
- Dashboard
- Logs: `data/logs.jsonl`
- Alerts config: `config/alert_rules.yaml`
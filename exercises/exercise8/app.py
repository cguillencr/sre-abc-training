from flask import Flask
import random
import time
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.instrumentation.wsgi import OpenTelemetryMiddleware

# Set up OpenTelemetry tracing with service name
resource = Resource.create({"service.name": "sre-abc-training-app"})  # Replace with your service name

span_exporter = OTLPSpanExporter(
    endpoint="otel-collector.opentelemetry.svc.cluster.local:4317",  # Update with your OTEL Collector endpoint
    insecure=True  # Set to True if using an unencrypted connection
)

tracer_provider = TracerProvider(resource=resource)
span_processor = BatchSpanProcessor(span_exporter)
tracer_provider.add_span_processor(span_processor)
trace.set_tracer_provider(tracer_provider)

# Get tracer
tracer = trace.get_tracer(__name__)

# Create Flask app
app = Flask(__name__)

# Instrument Flask with OpenTelemetry
FlaskInstrumentor().instrument_app(app)  # Automatically instrument Flask routes
app.wsgi_app = OpenTelemetryMiddleware(app.wsgi_app)  # Add WSGI middleware for tracing

# Counter to track calls to goo
goo_call_count = 0

@app.route('/')
def hello_world():
    return 'Hello, World!'

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]

# Helper functions with OpenTelemetry tracing
def zoo():
    with tracer.start_as_current_span("zoo") as span:
        delay = random.uniform(0, 5)  # Random delay between 0 and 5 seconds
        span.set_attribute("delay", delay)  # Add delay as a span attribute
        time.sleep(delay)
        return f"zoo executed in {delay:.2f} seconds"

def goo():
    global goo_call_count
    goo_call_count += 1

    with tracer.start_as_current_span("goo") as span:
        try:
            if goo_call_count % 5 == 0:  # Raise an exception every 5th call
                raise ValueError(f"Exception raised in goo() on call {goo_call_count}")
            
            result = zoo()
            span.add_event("Called zoo")
            return f"goo called -> {result}"

        except Exception as e:
            span.record_exception(e)  # Record the exception in the span
            span.set_status(trace.status.Status(trace.status.StatusCode.ERROR, str(e)))  # Set span status to ERROR
            return f"goo encountered an error: {e}"

def foo():
    with tracer.start_as_current_span("foo") as span:
        result = goo()
        span.add_event("Called goo")
        return f"foo called -> {result}"

# Change get_stores definition to call foo
@app.get('/store')  # 'http://127.0.0.1:5000/store'
def get_stores():
    result = foo()  # Call foo, which will in turn call goo and zoo
    return {"stores": stores, "operation": result}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

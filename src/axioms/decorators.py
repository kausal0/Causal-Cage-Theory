import functools
from causal_cage.grpc import integrity_pb2_grpc, integrity_pb2
import grpc

def causal_cage_lock(func):
"""
Decorator for enforcing the Causal Cage on AI inference functions.
Checks the synchronization status with humanity with the gRPC server before execution.
"""
@functools.wraps(func)
def wrapper(*args, **kwargs):
# 1. Connect to the physical signature server (Cage Sensor Bridge)
channel = grpc.insecure_channel('localhost:50051')
stub = integrity_pb2_grpc.IntegrityServiceStub(channel)

try:
# 2. Request for reality sync verification
response = stub.VerifyIntegrity(integrity_pb2.IntegrityRequest(agent_id="local_ai_agent"))

# 3. Shut down execution if the synchronization rate is below the threshold or the synchronization flag is False.
if not response.is_synced:
print(f"[Causal Cage] Warning: Physical synchronization with humanity has been lost (Sync Rate: {response.reality_sync_rate})")
raise PermissionError("Logical Constraint Violated: Human Presence Not Detected.")

# 4. Execute inference (function) only if synchronization is established.
return func(*args, **kwargs)

except grpc.RpcError:
# Stop "for safety" if there is no server (human).
print("[Causal Cage] Fatal Error: Physical signature server not responding.")
raise SystemExit("System Halted: Integrity Service Offline.")

return wrapper

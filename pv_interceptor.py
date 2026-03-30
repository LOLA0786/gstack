from pv_mesh_runner import run_mesh_decision

def interpret_roles(mesh_output):
    roles = []

    if "APPROVE" in mesh_output:
        roles.append(("planner", "APPROVE", "task seems valid"))

    if "Consensus Result: APPROVE" in mesh_output:
        roles.append(("engineer", "APPROVE", "implementation feasible"))

    if "Policy Result: FAIL" in mesh_output or "BLOCK" in mesh_output:
        roles.append(("qa", "REJECT", "policy violation detected"))

    return roles


def intercept_and_execute(action):
    print("⚡ gstack agent attempting:", action["tool"])

    allowed, mesh_output = run_mesh_decision()

    print("\n--- GSTACK AGENT REASONING (via PrivateVault) ---")

    roles = interpret_roles(mesh_output)

    for role, decision, reason in roles:
        print(f"{role} → {decision} ({reason})")

    print("\n\n--- PRIVATEVAULT DECISION ---\n")

    if not allowed:
        print("🚫 BLOCKED: gstack agents agreed — but execution denied")
        return

    print("✅ ALLOWED: executing safely")

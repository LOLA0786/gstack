from pv_interceptor import intercept_and_execute

def gstack_engineer_agent():
    print("🛠️ gstack agent output (simulated)")

    return {
        "tool": "stripe.customers.create",
        "params": {"email": "test@example.com"}
    }

def main():
    action = gstack_engineer_agent()

    # THIS is the key — instead of executing directly,
    # we pass through PrivateVault
    intercept_and_execute(action)

if __name__ == "__main__":
    main()

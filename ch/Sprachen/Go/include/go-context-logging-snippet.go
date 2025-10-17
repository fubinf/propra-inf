func withRequestId(ctx context.Context, id string) context.Context {
    // requestId zum Kontext hinzufügen
}

func getRequestId(ctx context.Context) string {
    // requestId aus dem Kontext auslesen
}

func log(ctx context.Context, message string) {
    id := getRequestId(ctx)
    fmt.Printf("[RequestId: %s] %s\n", id, message)
}

func validateOrder(ctx context.Context, orderId int) bool {
    log(ctx, fmt.Sprintf("Validating order %d", orderId))
    return orderId > 0
}

func processPayment(ctx context.Context, amount float64) {
    log(ctx, fmt.Sprintf("Processing payment of $%.2f", amount))
}

func shipOrder(ctx context.Context, orderId int) {
    log(ctx, fmt.Sprintf("Shipping order %d", orderId))
}

func handleOrder(ctx context.Context, orderId int, amount float64) {
    if validateOrder(ctx, orderId) {
        processPayment(ctx, amount)
        shipOrder(ctx, orderId)
    }
}

func simulateRequest() {
    r := rand.New(rand.NewSource(42))
    requestId := fmt.Sprintf("REQ-%d", r.Intn(10000))
    ctx := withRequestId(context.Background(), requestId)

    handleOrder(ctx, 12345, 99.99)
}


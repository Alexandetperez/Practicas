# 17. Si una persona (Antonio) deposita $1000 al 8% y otra (Marco) deposita $2000 al 3%, ¿cuántos años deberán pasar para que Antonio tenga más dinero que Marco?

def persona (marco, antonio, antonio_interes):
    marco_total = marco * (1 + antonio_interes)
    total_años= 0
    while antonio <= marco_total:
        antonio *= (1 + antonio_interes)
        marco *= (1 + antonio_interes)
        total_años += 1
    return total_años
marco = 2000
antonio = 1000
antonio_interes = 0.08
años = persona (marco, antonio, antonio_interes)
print("Antonio tendrá más dinero que Marco en aproximadamente", años, "años.")

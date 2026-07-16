import pandas as pd

# ===============================
# Load Dataset
# ===============================

df = pd.read_csv("Retail_Store_Analytics_With_Footfall.csv")

# ===============================
# Date & Time Formatting
# ===============================

df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")
df["Time"] = pd.to_datetime(df["Time"], errors="coerce")

# ===============================
# Create Time Block
# ===============================

def time_slot(hour):
    if 6 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 16:
        return "Afternoon"
    elif 16 <= hour < 20:
        return "Evening"
    else:
        return "Night"

df["Time_Block"] = df["Time"].dt.hour.apply(time_slot)

# ===============================
# Lowest & Highest Footfall Day
# ===============================

lowest_footfall_day = (
    df["Transaction_ID"]
    .groupby(df["Day"])
    .count()
    .idxmin()
)

highest_footfall_day = (
    df["Transaction_ID"]
    .groupby(df["Day"])
    .count()
    .idxmax()
)

# ===============================
# Average Weekday Footfall
# ===============================

weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday"]

avg_weekday_footfall = (
    df[df["Day"].isin(weekdays)]["Transaction_ID"]
    .groupby(df[df["Day"].isin(weekdays)]["Day"])
    .count()
    .mean()
    .round(2)
)

# ===============================
# Transactions Per Day
# ===============================

transactions_per_day = (
    df["Transaction_ID"]
    .groupby(df["Day"])
    .count()
)

# ===============================
# Peak & Lowest Footfall Hours
# ===============================

hour = df["Time"].dt.hour

peak_hour = (
    df["Transaction_ID"]
    .groupby(hour)
    .count()
    .idxmax()
)

lowest_hour = (
    df["Transaction_ID"]
    .groupby(hour)
    .count()
    .idxmin()
)

# ===============================
# Purchased / Not Purchased
# ===============================

purchased = (
    df[df["Customer_Status"] == "Purchased"]
    .shape[0]
)

not_purchased = (
    df[df["Customer_Status"] == "Left Without Purchase"]
    .shape[0]
)

# ===============================
# Total Revenue
# ===============================

total_sales = df["Bill_Amount"].sum()

# ===============================
# Sales Per Day & Time
# ===============================

sales_per_day = (
    df.groupby(["Day","Time_Block"])["Bill_Amount"]
      .sum()
      .unstack(fill_value=0)
)

# ===============================
# Highest & Lowest Sales Day
# ===============================

sales_day = (
    df.groupby("Day")["Bill_Amount"]
      .sum()
)

highest_sales_day = sales_day.idxmax()
lowest_sales_day = sales_day.idxmin()

# ===============================
# Best Selling Product
# ===============================

best_product = (
    df.groupby("Product")["Quantity"]
      .sum()
      .idxmax()
)

# ===============================
# Top Revenue Category
# ===============================

top_category = (
    df.groupby("Category")["Bill_Amount"]
      .sum()
      .idxmax()
)

# ===============================
# Payment Analysis
# ===============================

payment_mode = (
    df["Payment_Mode"]
      .value_counts()
      .idxmax()
)

# ===============================
# Average Sale Per Customer
# ===============================

average_sale = round(df["Bill_Amount"].mean(),2)

# ===============================
# Print Results
# ===============================

print("="*60)
print("        RETAIL STORE ANALYTICS REPORT")
print("="*60)

print("\nLowest Footfall Day :", lowest_footfall_day)

print("Highest Footfall Day :", highest_footfall_day)

print("Average Weekday Footfall :", avg_weekday_footfall)

print("\nTransactions Per Day\n")
print(transactions_per_day)

print("\nPeak Footfall Hour :", peak_hour,":00")

print("Lowest Footfall Hour :", lowest_hour,":00")

print("\nPurchased Customers :", purchased)

print("Customers Left Without Purchase :", not_purchased)

print("\nTotal Revenue : ₹", total_sales)

print("\nHighest Sales Day :", highest_sales_day)

print("Lowest Sales Day :", lowest_sales_day)

print("\nBest Selling Product :", best_product)

print("Top Revenue Category :", top_category)

print("Most Preferred Payment Mode :", payment_mode)

print("Average Sale Per Customer : ₹", average_sale)

print("\n========== SALES PER DAY ==========\n")
print(sales_per_day)

print("\n===================================")
print("        END OF REPORT")
print("===================================")

# ==========================================
# Suggestions Menu
# ==========================================

suggestions = []

def print_suggestions():
    print("\nSuggestions:")
    for i in suggestions:
        print("•", i)

while True:

    print("\n========== MENU ==========")
    print("1. Day & Time Wise Suggestions")
    print("2. Show Analytics Report")
    print("3. Exit")

    choice = int(input("Enter your choice (1-3): "))

    if choice == 3:
        print("Exiting Program...")
        break

    match choice:

        # ---------------------------------
        # Day & Time Suggestions
        # ---------------------------------

        case 1:

            suggestions.clear()

            user_day = input("Enter Day (Monday-Sunday): ").strip().capitalize()
            user_time = input("Enter Time (Morning/Afternoon/Evening/Night): ").strip().capitalize()

            # ---------- Day Suggestions ----------

            if user_day == highest_footfall_day:
                suggestions.append(f"{user_day} has the highest footfall.")
                suggestions.append("Increase staff members.")
                suggestions.append("Keep extra stock available.")
                suggestions.append("Run combo offers to increase sales.")
                suggestions.append("Open all billing counters.")

            elif user_day == lowest_footfall_day:
                suggestions.append(f"{user_day} has the lowest footfall.")
                suggestions.append("Provide discounts to attract customers.")
                suggestions.append("Reduce staff during slow hours.")
                suggestions.append("Schedule cleaning and maintenance.")
                suggestions.append("Promote offers on social media.")

            else:
                suggestions.append(f"{user_day} has average customer traffic.")
                suggestions.append("Maintain normal inventory.")
                suggestions.append("Monitor customer demand.")

            # ---------- Time Suggestions ----------

            if user_time == "Morning":
                suggestions.append("Offer breakfast and tea combos.")
                suggestions.append("Display fresh products near entrance.")
                suggestions.append("Keep counters fully operational.")

            elif user_time == "Afternoon":
                suggestions.append("Launch lunch-time discounts.")
                suggestions.append("Promote combo meal offers.")
                suggestions.append("Restock fast-selling items.")

            elif user_time == "Evening":
                suggestions.append("Increase cashier staff.")
                suggestions.append("Keep popular products ready.")
                suggestions.append("Run Happy Hour discounts.")

            elif user_time == "Night":
                suggestions.append("Offer clearance sale discounts.")
                suggestions.append("Prepare stock for next day.")
                suggestions.append("Begin cleaning activities.")

            else:
                suggestions.append("Invalid Time Entered.")

            print_suggestions()

        # ---------------------------------
        # Show Complete Report
        # ---------------------------------

        case 2:

            print("\n========== RETAIL STORE REPORT ==========\n")

            print("Lowest Footfall Day :", lowest_footfall_day)
            print("Highest Footfall Day :", highest_footfall_day)
            print("Average Weekday Footfall :", avg_weekday_footfall)

            print("\nTransactions Per Day")
            print(transactions_per_day)

            print("\nPeak Footfall Hour :", peak_hour, ":00")
            print("Lowest Footfall Hour :", lowest_hour, ":00")

            print("\nPurchased Customers :", purchased)
            print("Customers Left Without Purchase :", not_purchased)

            print("\nTotal Revenue : ₹", total_sales)

            print("\nHighest Sales Day :", highest_sales_day)
            print("Lowest Sales Day :", lowest_sales_day)

            print("\nBest Selling Product :", best_product)
            print("Top Revenue Category :", top_category)
            print("Most Preferred Payment Mode :", payment_mode)

            print("\nAverage Sale Per Customer : ₹", average_sale)

            print("\n========== SALES PER DAY ==========\n")
            print(sales_per_day)

        case _:
            print("Invalid Choice!")
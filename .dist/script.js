function showSection(id) {
    document.querySelectorAll(".card").forEach(c => c.classList.add("hidden"));
    if (id !== "savings" && id !== "totalIncome" && id !== "totalExpense") {
        document.getElementById(id).classList.remove("hidden");
    }

    if (id === "savings") {
        showOutput("Calling → tt.total()");
    }
    if (id === "totalIncome") {
        showOutput("Calling → dv.incomes()");
    }
    if (id === "totalExpense") {
        showOutput("Calling → dv.expenses()");
    }
}

function saveExpense() {
    const data = {
        name: expName.value,
        category: expCategory.value,
        amount: expAmount.value,
        date: expDate.value
    };

    showOutput(
`Expense saved:
${data.name} | ${data.category} | ${data.amount} | ${data.date}

Saved to expenses.csv`
    );
}

function saveIncome() {
    const data = {
        amount1: incAmount.value,
        date: incDate.value
    };

    showOutput(
`Income saved:
${data.amount1} | ${data.date}

Saved to income.csv`
    );
}

function showOutput(text) {
    document.getElementById("output").classList.remove("hidden");
    document.getElementById("console").textContent += text + "\n\n";
}

function exitApp() {
    showOutput("Program exited");
}

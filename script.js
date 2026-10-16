async function loadAgentResults() {
  const container = document.getElementById("rfi-results");

  try {
    const response = await fetch("./data/agent_results.json");

    if (!response.ok) {
      throw new Error("Could not load agent results.");
    }

    const results = await response.json();

    // Summary
    const totalRFIs = results.length;

    const responseCount = results.filter(
      item => item.needs_response === true
    ).length;

    const highRiskCount = results.filter(
      item => item.contractual_risk === "high"
    ).length;

    const duplicateCount = results.filter(
      item => item.duplicate_of !== null
    ).length;

    document.getElementById("total-rfis").textContent = totalRFIs;
    document.getElementById("response-count").textContent = responseCount;
    document.getElementById("high-risk-count").textContent = highRiskCount;
    document.getElementById("duplicate-count").textContent = duplicateCount;

    // Clear loading text
    container.innerHTML = "";

    // Create one card per RFI
    results.forEach(result => {
      const card = document.createElement("article");
      card.className = "rfi-card";

      const dueText = result.due
        ? formatLabel(result.due)
        : "Not specified";

      const duplicateText = result.duplicate_of
        ? `RFI #${result.duplicate_of}`
        : "None";

      card.innerHTML = `
        <div class="rfi-card-header">

          <div>
            <p class="rfi-label">REQUEST FOR INFORMATION</p>
            <h3>RFI #${result.rfi_id}</h3>
          </div>

          <span class="priority-badge priority-${result.priority}">
            Priority ${result.priority}
          </span>

        </div>

        <div class="triage-grid">

          <div class="triage-item">
            <span>Needs Response</span>
            <strong>${result.needs_response ? "Yes" : "No"}</strong>
          </div>

          <div class="triage-item">
            <span>Root Cause</span>
            <strong>${formatLabel(result.root_cause)}</strong>
          </div>

          <div class="triage-item">
            <span>Responder</span>
            <strong>${formatLabel(result.responder)}</strong>
          </div>

          <div class="triage-item">
            <span>Due</span>
            <strong>${dueText}</strong>
          </div>

          <div class="triage-item">
            <span>Contractual Risk</span>
            <strong>${formatLabel(result.contractual_risk)}</strong>
          </div>

          <div class="triage-item">
            <span>Duplicate Of</span>
            <strong>${duplicateText}</strong>
          </div>

        </div>

        <div class="risk-reason">
          <span>Risk Reason</span>
          <p>${result.risk_reason || "No risk reason provided."}</p>
        </div>
      `;

      container.appendChild(card);
    });

  } catch (error) {
    console.error(error);

    container.innerHTML = `
      <div class="error-message">
        Agent results could not be loaded.
      </div>
    `;
  }
}


function formatLabel(value) {
  if (value === null || value === undefined) {
    return "Not specified";
  }

  return String(value)
    .replaceAll("_", " ")
    .replace(/\b\w/g, char => char.toUpperCase());
}


loadAgentResults();
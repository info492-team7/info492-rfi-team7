// ============================================================
// INFO 492 C · GC Team 7
// Demo 1 + Demo 2 Web App
// ============================================================


// ------------------------------------------------------------
// HELPER FUNCTIONS
// ------------------------------------------------------------

function formatLabel(value) {
  if (value === null || value === undefined || value === "") {
    return "—";
  }

  return String(value)
    .replace(/_/g, " ")
    .replace(/\b\w/g, (letter) => letter.toUpperCase());
}


function formatYesNo(value) {
  return value ? "Yes" : "No";
}


function formatDuplicate(value) {
  if (!value) {
    return "No";
  }

  return `Yes — RFI #${value}`;
}


function getPriorityClass(priority) {
  if (priority === 1) return "priority-1";
  if (priority === 2) return "priority-2";
  if (priority === 3) return "priority-3";

  return "";
}


// ============================================================
// DEMO 1
// Brush Creek
// ============================================================

async function loadDemo1() {
  const resultsContainer = document.getElementById("rfi-results");

  if (!resultsContainer) {
    return;
  }

  try {
    const response = await fetch(
      "./data/brush_creek/agent_results.json"
    );

    if (!response.ok) {
      throw new Error("Could not load Demo 1 results.");
    }

    const data = await response.json();

    updateDemo1Summary(data);
    renderDemo1Results(data);

  } catch (error) {
    console.error("Demo 1 error:", error);

    resultsContainer.innerHTML = `
      <div class="result-panel warning-panel">
        <h3>Demo 1 results could not be loaded.</h3>
        <p>Please check the Brush Creek result file.</p>
      </div>
    `;
  }
}


function updateDemo1Summary(data) {
  const total = data.length;

  const responseCount = data.filter(
    (item) => item.needs_response === true
  ).length;

  const highRiskCount = data.filter(
    (item) =>
      String(item.contractual_risk).toLowerCase() === "high"
  ).length;

  const duplicateCount = data.filter(
    (item) => item.duplicate_of
  ).length;


  const totalElement = document.getElementById("total-rfis");
  const responseElement = document.getElementById("response-count");
  const highRiskElement = document.getElementById("high-risk-count");
  const duplicateElement = document.getElementById("duplicate-count");


  if (totalElement) {
    totalElement.textContent = total;
  }

  if (responseElement) {
    responseElement.textContent = responseCount;
  }

  if (highRiskElement) {
    highRiskElement.textContent = highRiskCount;
  }

  if (duplicateElement) {
    duplicateElement.textContent = duplicateCount;
  }
}


function renderDemo1Results(data) {
  const container = document.getElementById("rfi-results");

  if (!container) {
    return;
  }

  container.innerHTML = data
    .map((item) => {
      return `
        <article class="rfi-card">

          <div class="rfi-card-header">

            <div>
              <p class="result-label">
                RFI #${item.rfi_id}
              </p>

              <h3>
                ${formatLabel(item.root_cause)}
              </h3>
            </div>

            <span class="priority-badge ${getPriorityClass(item.priority)}">
              Priority ${item.priority}
            </span>

          </div>


          <div class="triage-grid">

            <div class="triage-item">
              <strong>Needs Response</strong>
              <span>${formatYesNo(item.needs_response)}</span>
            </div>

            <div class="triage-item">
              <strong>Root Cause</strong>
              <span>${formatLabel(item.root_cause)}</span>
            </div>

            <div class="triage-item">
              <strong>Responder</strong>
              <span>${formatLabel(item.responder)}</span>
            </div>

            <div class="triage-item">
              <strong>Due</strong>
              <span>${formatLabel(item.due)}</span>
            </div>

            <div class="triage-item">
              <strong>Contractual Risk</strong>
              <span>${formatLabel(item.contractual_risk)}</span>
            </div>

            <div class="triage-item">
              <strong>Duplicate</strong>
              <span>${formatDuplicate(item.duplicate_of)}</span>
            </div>

          </div>


          <div class="risk-reason">

            <strong>Risk Reason</strong>

            <p>
              ${item.risk_reason || "No explanation provided."}
            </p>

          </div>

        </article>
      `;
    })
    .join("");
}


// ============================================================
// DEMO 2
// Haggett Hall
// ============================================================

let demo2Results = [];
let demo2Questions = [];
let allHaggettRFIs = [];


// ------------------------------------------------------------
// LOAD DEMO 2 DATA
// ------------------------------------------------------------

async function loadDemo2() {
  const container = document.getElementById("demo2-results");

  if (!container) {
    return;
  }

  try {
    const [
      run1Response,
      testSetResponse,
      allRFIsResponse
    ] = await Promise.all([
      fetch("./results/run1.json"),
      fetch("./data/rfi_test_set.json"),
      fetch("./data/haggett_all_rfis.json")
    ]);


    if (
      !run1Response.ok ||
      !testSetResponse.ok ||
      !allRFIsResponse.ok
    ) {
      throw new Error("Could not load Demo 2 data.");
    }


    demo2Results = await run1Response.json();

    demo2Questions = await testSetResponse.json();

    allHaggettRFIs = await allRFIsResponse.json();


    renderDemo2Results(demo2Results);

    populateAskAISelector(demo2Questions);


  } catch (error) {
    console.error("Demo 2 error:", error);

    container.innerHTML = `
      <div class="result-panel warning-panel">

        <p class="result-label">
          DATA ERROR
        </p>

        <h3>
          Agent v2 results could not be loaded.
        </h3>

        <p>
          Please confirm that run1.json and the Haggett Hall data files
          are available in the repository.
        </p>

      </div>
    `;
  }
}


// ------------------------------------------------------------
// DISPLAY THE 10 AGENT V2 RESULTS
// ------------------------------------------------------------

function renderDemo2Results(data) {
  const container = document.getElementById("demo2-results");

  if (!container) {
    return;
  }


  container.innerHTML = data
    .map((item) => {

      const questionData = demo2Questions.find(
        (question) =>
          String(question.rfi_id) === String(item.rfi_id)
      );


      const title = questionData
        ? questionData.topic
        : `RFI #${item.rfi_id}`;


      return `
        <article class="rfi-card">

          <div class="rfi-card-header">

            <div>

              <p class="result-label">
                RFI #${item.rfi_id}
              </p>

              <h3>
                ${title}
              </h3>

            </div>


            <span class="priority-badge ${getPriorityClass(item.priority)}">
              Priority ${item.priority}
            </span>

          </div>


          <div class="triage-grid">

            <div class="triage-item">

              <strong>
                Needs Response
              </strong>

              <span>
                ${formatYesNo(item.needs_response)}
              </span>

            </div>


            <div class="triage-item">

              <strong>
                Root Cause
              </strong>

              <span>
                ${formatLabel(item.root_cause)}
              </span>

            </div>


            <div class="triage-item">

              <strong>
                Responder
              </strong>

              <span>
                ${formatLabel(item.responder)}
              </span>

            </div>


            <div class="triage-item">

              <strong>
                Response Timing
              </strong>

              <span>
                ${item.due ? `${item.due} days` : "—"}
              </span>

            </div>


            <div class="triage-item">

              <strong>
                Contractual Risk
              </strong>

              <span>
                ${formatLabel(item.contractual_risk)}
              </span>

            </div>


            <div class="triage-item">

              <strong>
                Follow-Up
              </strong>

              <span>
                ${formatDuplicate(item.duplicate_of)}
              </span>

            </div>

          </div>


          <div class="risk-reason">

            <strong>
              Agent Reasoning
            </strong>

            <p>
              ${item.risk_reason || "No explanation provided."}
            </p>

          </div>

        </article>
      `;
    })
    .join("");
}


// ============================================================
// ASK AI
// ============================================================

function populateAskAISelector(questions) {
  const select = document.getElementById("ask-rfi-select");

  if (!select) {
    return;
  }


  questions.forEach((item) => {

    const option = document.createElement("option");

    option.value = item.rfi_id;

    option.textContent =
      `RFI #${item.rfi_id} — ${item.topic}`;

    select.appendChild(option);

  });
}


// ------------------------------------------------------------
// FIND EARLIER RFI EVIDENCE
// ------------------------------------------------------------

function findEarlierRFI(rfiId) {
  return allHaggettRFIs.find(
    (item) =>
      String(item.rfi_id) === String(rfiId)
  );
}


// ------------------------------------------------------------
// SHOW ASK AI RESULT
// ------------------------------------------------------------

function showAskAIResult() {
  const select = document.getElementById("ask-rfi-select");

  if (!select) {
    return;
  }


  const selectedId = select.value;


  if (!selectedId) {
    alert("Please select an RFI first.");
    return;
  }


  const question = demo2Questions.find(
    (item) =>
      String(item.rfi_id) === String(selectedId)
  );


  const result = demo2Results.find(
    (item) =>
      String(item.rfi_id) === String(selectedId)
  );


  if (!question || !result) {
    alert("The selected RFI result could not be found.");
    return;
  }


  // ----------------------------------------------------------
  // ORIGINAL QUESTION
  // ----------------------------------------------------------

  const questionPanel =
    document.getElementById("ask-ai-question");

  const answerPanel =
    document.getElementById("ask-ai-answer");


  document.getElementById("ask-ai-title").textContent =
    `RFI #${question.rfi_id} — ${question.topic}`;


  document.getElementById("ask-ai-question-text").textContent =
    question.question;


  // ----------------------------------------------------------
  // AGENT ASSESSMENT
  // ----------------------------------------------------------

  document.getElementById("ask-priority").textContent =
    `Priority ${result.priority}`;


  document.getElementById("ask-responder").textContent =
    formatLabel(result.responder);


  document.getElementById("ask-root-cause").textContent =
    formatLabel(result.root_cause);


  document.getElementById("ask-risk").textContent =
    formatLabel(result.contractual_risk);


  document.getElementById("ask-due").textContent =
    result.due
      ? `${result.due} days`
      : "—";


  document.getElementById("ask-duplicate").textContent =
    result.duplicate_of
      ? `Follow-up to RFI #${result.duplicate_of}`
      : "No earlier RFI identified";


  document.getElementById("ask-reason").textContent =
    result.risk_reason || "No explanation provided.";


  // ----------------------------------------------------------
  // EVIDENCE
  // ----------------------------------------------------------

  const evidenceElement =
    document.getElementById("ask-evidence");


  if (result.duplicate_of) {

    const earlierRFI =
      findEarlierRFI(result.duplicate_of);


    if (earlierRFI) {

      evidenceElement.innerHTML = `
        <strong>
          Current RFI evidence:
        </strong>

        ${question.question}

        <br><br>

        <strong>
          Earlier related RFI #${earlierRFI.rfi_id}:
        </strong>

        ${earlierRFI.question}
      `;

    } else {

      evidenceElement.textContent =
        `The current question references earlier RFI #${result.duplicate_of}.`;

    }

  } else {

    evidenceElement.textContent =
      question.question;

  }


  // ----------------------------------------------------------
  // SHOW PANELS
  // ----------------------------------------------------------

  questionPanel.style.display = "block";

  answerPanel.style.display = "block";


  answerPanel.scrollIntoView({
    behavior: "smooth",
    block: "nearest"
  });
}


// ============================================================
// PAGE INITIALIZATION
// ============================================================

document.addEventListener("DOMContentLoaded", () => {

  // Demo 1
  loadDemo1();


  // Demo 2
  loadDemo2();


  // Ask AI button
  const askButton =
    document.getElementById("ask-ai-button");


  if (askButton) {

    askButton.addEventListener(
      "click",
      showAskAIResult
    );

  }

});
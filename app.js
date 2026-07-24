import { parseReadme } from "./content-parser.js";

const REPO = "akirakai/awesome-flux3";
const BRANCH = "main";
const RAW_README = `https://raw.githubusercontent.com/${REPO}/${BRANCH}/README.md`;
const state = { entries: [], query: "", filter: "all", sort: "latest" };
const els = {
  grid: document.querySelector("#video-grid"),
  loading: document.querySelector("#collection-state"),
  empty: document.querySelector("#empty-state"),
  count: document.querySelector("#entry-count"),
  updated: document.querySelector("#last-updated"),
  sync: document.querySelector("#sync-state"),
  search: document.querySelector("#search-input"),
  sort: document.querySelector("#sort-select"),
  filters: [...document.querySelectorAll(".filter")],
  template: document.querySelector("#video-card-template"),
};

function promptLabel(provenance) {
  if (provenance === "verbatim_in_post") return ["Prompt available", "available"];
  if (provenance === "mentioned_not_in_post") return ["Prompt referenced", "referenced"];
  return ["No prompt", "missing"];
}

function displayDate(value) {
  if (!value || value === "Date unavailable") return value;
  const date = new Date(`${value}T00:00:00Z`);
  if (Number.isNaN(date.getTime())) return value;
  return new Intl.DateTimeFormat("en", { year: "numeric", month: "short", day: "numeric", timeZone: "UTC" }).format(date);
}

function renderCard(entry) {
  const fragment = els.template.content.cloneNode(true);
  const sourceUrl = entry.sourceUrl || `https://github.com/${REPO}/blob/${BRANCH}/README.md`;
  const [label, className] = promptLabel(entry.provenance);
  fragment.querySelector(".visual-number").textContent = String(entry.order).padStart(2, "0");
  fragment.querySelector(".play-link").href = sourceUrl;
  fragment.querySelector(".published").textContent = displayDate(entry.published);
  const badge = fragment.querySelector(".prompt-badge");
  badge.textContent = label;
  badge.classList.add(className);
  fragment.querySelector(".card-title").textContent = entry.title;
  const creator = fragment.querySelector(".creator-link");
  creator.textContent = entry.creator;
  creator.href = entry.creatorUrl || sourceUrl;
  fragment.querySelector(".summary").textContent = entry.summary;
  fragment.querySelector(".attribution-row dd").textContent = entry.attribution;
  fragment.querySelector(".workflow-row dd").textContent = entry.workflow;
  fragment.querySelector(".prompt-content").textContent = entry.prompt ? `${entry.provenanceText}\n\n${entry.prompt}` : entry.provenanceText;
  fragment.querySelector(".why-row p").textContent = entry.why;
  fragment.querySelector(".source-button").href = sourceUrl;
  return fragment;
}

function getVisibleEntries() {
  const query = state.query.trim().toLowerCase();
  let entries = state.entries.filter((entry) => {
    const haystack = [entry.title, entry.creator, entry.summary, entry.workflow, entry.prompt, entry.why].join(" ").toLowerCase();
    const matchesQuery = !query || haystack.includes(query);
    const matchesFilter = state.filter === "all" || (state.filter === "with-prompt" && entry.provenance === "verbatim_in_post") || (state.filter === "without-prompt" && entry.provenance !== "verbatim_in_post");
    return matchesQuery && matchesFilter;
  });
  if (state.sort === "latest" || state.sort === "oldest") {
    entries = [...entries].sort((a, b) => {
      const aTime = Date.parse(a.published) || 0;
      const bTime = Date.parse(b.published) || 0;
      return state.sort === "latest" ? bTime - aTime : aTime - bTime;
    });
  } else entries = [...entries].sort((a, b) => a.order - b.order);
  return entries;
}

function render() {
  const entries = getVisibleEntries();
  els.grid.replaceChildren(...entries.map(renderCard));
  els.grid.hidden = entries.length === 0;
  els.empty.hidden = entries.length !== 0;
}

function setSync(status, label) {
  els.sync.className = `status-pill ${status}`;
  els.sync.textContent = label;
}

async function loadReadme() {
  try {
    const response = await fetch(`${RAW_README}?v=${Date.now()}`, { cache: "no-store" });
    if (!response.ok) throw new Error(`GitHub returned ${response.status}`);
    const parsed = parseReadme(await response.text());
    state.entries = parsed.entries;
    els.count.textContent = parsed.entries.length || parsed.declaredCount;
    els.updated.textContent = parsed.updated;
    els.loading.hidden = true;
    setSync("online", "Live");
    render();
  } catch (error) {
    console.error(error);
    els.loading.innerHTML = `<span class="empty-glyph" aria-hidden="true">!</span><strong>Could not load the GitHub README</strong><span>Open the repository directly or refresh this page.</span>`;
    setSync("error", "Offline");
  }
}

els.search.addEventListener("input", (event) => { state.query = event.target.value; render(); });
els.sort.addEventListener("change", (event) => { state.sort = event.target.value; render(); });
els.filters.forEach((button) => button.addEventListener("click", () => {
  state.filter = button.dataset.filter;
  els.filters.forEach((item) => item.classList.toggle("active", item === button));
  render();
}));
loadReadme();

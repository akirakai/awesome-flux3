export function cleanMarkdown(value = "") {
  return value
    .replace(/`([^`]+)`/g, "$1")
    .replace(/\*\*([^*]+)\*\*/g, "$1")
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, "$1")
    .replace(/\\([*_`])/g, "$1")
    .trim();
}

export function extractLink(value = "") {
  const match = value.match(/\[([^\]]+)\]\((https?:\/\/[^)]+)\)/);
  return match ? { label: cleanMarkdown(match[1]), url: match[2] } : null;
}

function parseFieldLines(body) {
  const fields = {};
  let currentKey = null;
  for (const line of body.split("\n")) {
    const bullet = line.match(/^-\s+\*\*([^:*]+):\*\*\s*(.*)$/);
    if (bullet) {
      currentKey = bullet[1].trim().toLowerCase();
      fields[currentKey] = bullet[2].trim();
      continue;
    }
    if (currentKey && /^\s{2,}\S/.test(line)) fields[currentKey] += `\n${line.trim()}`;
  }
  return fields;
}

export function parseReadme(markdown) {
  const updatedMatch = markdown.match(/_Last updated:\s*([^·\n]+?)\s*·\s*Entries:\s*(\d+)_/i);
  const curatedIndex = markdown.search(/^##\s+Curated videos\s*$/m);
  const curated = curatedIndex >= 0 ? markdown.slice(curatedIndex) : markdown;
  const headingRegex = /^###\s+(\d+)\.\s+(.+?)(?:\s+—\s+(.+))?\s*$/gm;
  const matches = [...curated.matchAll(headingRegex)];
  const entries = matches.map((match, index) => {
    const start = match.index + match[0].length;
    const end = index + 1 < matches.length ? matches[index + 1].index : curated.length;
    const fields = parseFieldLines(curated.slice(start, end));
    const creatorLink = extractLink(fields.creator);
    const sourceLink = extractLink(fields["original post"] || fields.source || "");
    const provenanceRaw = fields["prompt provenance"] || "not_provided";
    const provenance = provenanceRaw.match(/`?(verbatim_in_post|mentioned_not_in_post|not_provided)`?/i)?.[1] || "not_provided";
    return {
      order: Number(match[1]),
      title: cleanMarkdown(match[2]),
      creator: creatorLink?.label || cleanMarkdown(fields.creator || match[3] || "Unknown creator"),
      creatorUrl: creatorLink?.url || "",
      published: cleanMarkdown(fields.published || "Date unavailable"),
      sourceUrl: sourceLink?.url || "",
      attribution: cleanMarkdown(fields["model attribution"] || "Explicit FLUX.3 attribution recorded in the repository."),
      summary: cleanMarkdown(fields.summary || "No summary provided."),
      workflow: cleanMarkdown(fields["workflow/details"] || fields.workflow || "No workflow details provided."),
      provenance,
      provenanceText: cleanMarkdown(provenanceRaw),
      prompt: cleanMarkdown(fields.prompt || ""),
      why: cleanMarkdown(fields["why included"] || fields["quality rationale"] || "Selected for source quality and visual value."),
    };
  });
  return { updated: updatedMatch?.[1]?.trim() || "Unknown", declaredCount: Number(updatedMatch?.[2] || entries.length), entries };
}

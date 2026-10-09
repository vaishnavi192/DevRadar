import { useEffect, useState } from "react";

const sections = [
  "Overview",
  "Developer Problems",
  "Demand Signals",
  "Content Gaps",
  "GTM Recommendations",
];

function normalizeProblem(problem) {
  if (typeof problem === "string") {
    return { title: problem, description: "", meta: "" };
  }

  return {
    title: problem?.problem || problem?.title || problem?.name || "Developer problem",
    description:
      problem?.evidence ||
      problem?.description ||
      problem?.why_it_matters ||
      "",
    meta:
      problem?.frequency ||
      problem?.severity ||
      problem?.category ||
      "",
  };
}

function ResultCard({ number, title, description, meta }) {
  return (
    <div className="rounded-2xl border border-white/[0.08] bg-[#161d18] p-5">
      <div className="flex items-start gap-4">
        <span className="pt-0.5 font-sans text-[9px] tracking-[0.14em] text-[#69756b]">
          {String(number).padStart(2, "0")}
        </span>

        <div className="min-w-0 flex-1">
          <div className="text-[14px] leading-5 text-[#dfe5df]">
            {title}
          </div>

          {description && (
            <div className="mt-2 text-[12px] leading-5 text-[#8d9990]">
              {description}
            </div>
          )}

          {meta && (
            <div className="mt-3 font-sans text-[8px] uppercase tracking-[0.16em] text-[#7f8c82]">
              {meta}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

function ResearchProgress({ form, stage }) {
  const steps = [
    "Google searches analysed",
    "GitHub issues analysed",
    "YouTube videos analysed",
    "Search trends analysed",
    "Evidence clusters formed",
    "GTM intelligence generated",
  ];

  return (
    <div className="flex min-h-[600px] items-center justify-center p-8">
      <div className="w-full max-w-[920px] rounded-[26px] border border-white/65 bg-[#0b100d]/72 p-9 shadow-[0_24px_65px_rgba(0,0,0,0.34),0_1px_0_rgba(255,255,255,0.08)_inset] backdrop-blur-2xl">
        <div className="font-sans text-[8px] uppercase tracking-[0.2em] text-[#78847b]">
          Research in progress
        </div>

        <h3 className="mt-3 text-3xl font-medium tracking-[-0.04em] text-[#dfe5df]">
          Mapping {form.name || "the developer"} landscape
        </h3>

        <p className="mt-2 text-sm leading-6 text-[#8d9990]">
          Gathering evidence across the connected research sources.
        </p>

        <div className="mt-8 rounded-xl border border-white/[0.08] bg-[#080d0a] p-5 font-mono text-[11px] leading-7">
          <div className="text-[#9ca79e]">
            <span className="text-[#9F3832]">➜</span>{" "}
            devradar research {form.website || form.name || "target"}
          </div>

          <div className="mt-3 space-y-1">
            {steps.map((step, index) => (
              <div
                key={step}
                className={
                  index < stage ? "text-[#aab3ab]" : "text-[#4f5951]"
                }
              >
                <span className="mr-2">
                  {index < stage ? "✓" : "·"}
                </span>
                {step}
              </div>
            ))}
          </div>

          <div className="mt-4 text-[#69756b]">
            Research engine running...
          </div>
        </div>
      </div>
    </div>
  );
}

export default function ResearchTerminal({
  form,
  result,
  loading,
  error,
  activeSection,
  setActiveSection,
  updateField,
  handleSubmit,
  setResult,
}) {
  const [researchStage, setResearchStage] = useState(0);

  useEffect(() => {
    if (!loading) {
      setResearchStage(0);
      return;
    }

    setResearchStage(1);

    const timers = [
      setTimeout(() => setResearchStage(2), 900),
      setTimeout(() => setResearchStage(3), 1800),
      setTimeout(() => setResearchStage(4), 2700),
      setTimeout(() => setResearchStage(5), 3600),
      setTimeout(() => setResearchStage(6), 4700),
    ];

    return () => timers.forEach(clearTimeout);
  }, [loading]);

  const problems = result?.developer_problems || [];
  const demandSignals = result?.demand_signals || [];
  const contentGaps = result?.content_gaps || [];
  const recommendations = result?.gtm_recommendations || [];
  const conclusions = result?.conclusions || [];

  return (
    <section
        id="research"
        className="relative bg-[#D9DDD8] px-5 py-8 text-[#dfe5df] lg:px-10 lg:py-10"
      >
      <div className="mx-auto w-full max-w-[1740px]">
        <div className="mb-8">
          <h2 className="max-w-[900px] text-4xl font-medium tracking-[-0.05em] text-[#273229] sm:text-5xl">
            Find what developers are struggling with. Decide what to do next.
          </h2>

          <p className="mt-4 max-w-[650px] text-sm leading-6 text-[#68736a]">
            Trace the questions, conversations, and content shaping the
            developer market.
          </p>
        </div>

        <div className="overflow-hidden rounded-[30px] border border-white/55 bg-[#101410] shadow-[0_30px_90px_rgba(8,12,9,0.38)]">
          <div className="flex min-h-[650px]">
            <aside className="hidden w-[280px] shrink-0 border-r border-white/[0.08] bg-[#0d120f] md:block">
              <div className="border-b border-white/[0.08] px-6 py-6">
                <div className="font-sans text-[9px] uppercase tracking-[0.2em] text-[#8f9e91]">
                  Research
                </div>

                <div className="mt-2 text-xs text-[#c2c9c2]">
                  Developer landscape
                </div>
              </div>

              <div className="py-5">
                <div className="px-6 pb-3 font-sans text-[8px] uppercase tracking-[0.2em] text-[#7f8b82]">
                  Workspace
                </div>

                {sections.map((section) => (
                  <button
                    key={section}
                    type="button"
                    onClick={() => setActiveSection(section)}
                    className={`block w-full px-6 py-3 text-left text-[12px] ${
                      activeSection === section
                        ? "bg-[#8f9e9118] text-[#dfe5df] shadow-[inset_2px_0_0_#8f9e91]"
                        : "text-[#a5aea6] hover:bg-white/[0.05]"
                    }`}
                  >
                    {section}
                  </button>
                ))}
              </div>

              <div className="border-t border-white/[0.08] py-5">
                <div className="px-6 pb-3 font-sans text-[8px] uppercase tracking-[0.2em] text-[#7f8b82]">
                  Sources
                </div>

                {[
                  "Google Search",
                  "YouTube",
                  "GitHub",
                  "Search Trends",
                ].map((source) => (
                  <div
                    key={source}
                    className="flex items-center gap-3 px-6 py-2.5 text-[10px] text-[#667269]"
                  >
                    <span className="h-2 w-2 rounded-full bg-[#8f9e91]" />
                    {source}
                  </div>
                ))}
              </div>
            </aside>

            <div className="min-w-0 flex-1 bg-[#0d120f]">
              <div className="flex h-14 items-center justify-between border-b border-white/[0.08] px-6">
                <div className="flex items-center gap-2">
                  <span
                    className={`h-2 w-2 rounded-full ${
                      loading
                        ? "animate-pulse bg-[#9F3832]"
                        : "bg-[#9F3832]"
                    }`}
                  />

                  <span className="font-sans text-[9px] uppercase tracking-[0.18em] text-[#aab3ab]">
                    {loading
                      ? "Researching"
                      : result
                        ? "Research complete"
                        : "New research"}
                  </span>
                </div>

                <span className="font-sans text-[9px] text-[#9ca79e]">
                  ⌘ K
                </span>
              </div>

              {!result && !loading ? (
                <div className="flex min-h-[596px] items-center justify-center p-8 lg:p-12">
                  <form
                    onSubmit={handleSubmit}
                    className="w-full max-w-[920px] rounded-[26px] border border-white/65 bg-[#0b100d] p-9 shadow-[0_24px_65px_rgba(0,0,0,0.34)]"
                  >
                    <div className="mb-8">
                      <div className="font-sans text-[8px] uppercase tracking-[0.2em] text-[#78847b]">
                        New research
                      </div>

                      <h3 className="mt-3 text-3xl font-medium tracking-[-0.04em] text-[#dfe5df]">
                        What are developers telling us?
                      </h3>

                      <p className="mt-2 text-sm leading-6 text-[#8d9990]">
                        Enter a product and map the surrounding developer
                        landscape.
                      </p>
                    </div>

                    <div className="grid gap-5 sm:grid-cols-2">
                      <label>
                        <span className="mb-2 block font-sans text-[8px] uppercase tracking-[0.18em] text-[#69756b]">
                          Product
                        </span>

                        <input
                          name="name"
                          value={form.name}
                          onChange={updateField}
                          placeholder="e.g. SerpApi"
                          className="h-14 w-full rounded-xl border border-white/[0.10] bg-white/[0.045] px-4 text-base text-[#dce3dc] outline-none placeholder:text-[#68756b] focus:border-[#8f9e91]"
                        />
                      </label>

                      <label>
                        <span className="mb-2 block font-sans text-[8px] uppercase tracking-[0.18em] text-[#69756b]">
                          Website
                        </span>

                        <input
                          name="website"
                          value={form.website}
                          onChange={updateField}
                          placeholder="https://..."
                          className="h-14 w-full rounded-xl border border-white/[0.10] bg-white/[0.045] px-4 text-base text-[#dce3dc] outline-none placeholder:text-[#68756b] focus:border-[#8f9e91]"
                        />
                      </label>

                      <label className="sm:col-span-2">
                        <span className="mb-2 block font-sans text-[8px] uppercase tracking-[0.18em] text-[#69756b]">
                          Target audience
                        </span>

                        <input
                          name="targetAudience"
                          value={form.targetAudience}
                          onChange={updateField}
                          placeholder="e.g. Developers building AI products"
                          className="h-14 w-full rounded-xl border border-white/[0.10] bg-white/[0.045] px-4 text-base text-[#dce3dc] outline-none placeholder:text-[#68756b] focus:border-[#8f9e91]"
                        />
                      </label>

                      <label className="sm:col-span-2">
                        <span className="mb-2 block font-sans text-[8px] uppercase tracking-[0.18em] text-[#69756b]">
                          Primary goal
                        </span>

                        <select
                          value={form.primary_goal}
                          onChange={(event) =>
                            updateField({
                              target: {
                                name: "primary_goal",
                                value: event.target.value,
                              },
                            })
                          }
                          className="h-14 w-full rounded-xl border border-[#8f9e91] bg-transparent px-4 text-base text-[#d8ddd8] outline-none"
                        >
                          <option value="Developer acquisition">Developer acquisition</option>
                          <option value="Content strategy">Content strategy</option>
                          <option value="Developer activation">Developer activation</option>
                          <option value="Product research">Product research</option>
                          <option value="Competitive research">Competitive research</option>
                        </select>
                      </label>
                    </div>

                    {error && (
                      <div className="mt-5 rounded-xl border border-[#9a5f4b33] bg-[#a96d590d] px-4 py-3 text-xs text-[#875847]">
                        {error}
                      </div>
                    )}

                    <div className="mt-8 flex items-center justify-between border-t border-white/[0.08] pt-7">
                      <span className="hidden font-sans text-[8px] uppercase tracking-[0.16em] text-[#7f8c82] sm:block">
                        4 sources / 1 research engine
                      </span>

                      <button
                        type="submit"
                        disabled={loading}
                        className="group ml-auto flex h-12 items-center gap-3 rounded-full bg-[#9F3832] px-6 text-sm font-medium text-[#D9DDD8] transition hover:bg-[#8f302b] disabled:opacity-60"
                      >
                        Analyze landscape
                        <span className="transition-transform group-hover:translate-x-1">
                          →
                        </span>
                      </button>
                    </div>
                  </form>
                </div>
              ) : loading ? (
                <ResearchProgress form={form} stage={researchStage} />
              ) : (
                <div className="p-8 lg:p-10">
                  <div className="flex flex-wrap items-start justify-between gap-5 border-b border-white/[0.08] pb-7">
                    <div>
                      <div className="mb-3 flex items-center gap-2 font-sans text-[8px] uppercase tracking-[0.2em] text-[#7f8c82]">
                        <span className="h-1.5 w-1.5 rounded-full bg-[#8f9e91]" />
                        Research complete
                      </div>

                      <h3 className="text-2xl font-medium tracking-[-0.04em] text-[#dfe5df]">
                        {form.name}
                      </h3>

                      <p className="mt-2 text-xs text-[#7f8c82]">
                        Developer landscape → GTM intelligence
                      </p>
                    </div>

                    <button
                      type="button"
                      onClick={() => setResult(null)}
                      className="rounded-full border border-white/[0.12] px-3 py-2 font-sans text-[8px] uppercase tracking-[0.14em] text-[#8f9e91] hover:bg-white/[0.06]"
                    >
                      New research
                    </button>
                  </div>

                  <div className="flex flex-wrap gap-10 py-8">
                    {[
                      ["Problems", problems.length],
                      ["Demand", demandSignals.length],
                      ["Content gaps", contentGaps.length],
                      ["GTM moves", recommendations.length],
                    ].map(([label, value]) => (
                      <div key={label}>
                        <div className="text-xl text-[#dfe5df]">{value}</div>
                        <div className="font-sans text-[8px] uppercase tracking-[0.16em] text-[#7f8c82]">
                          {label}
                        </div>
                      </div>
                    ))}
                  </div>

                  <div className="space-y-3">
                    {activeSection === "Overview" &&
                      conclusions.map((conclusion, index) => (
                        <div
                          key={index}
                          className="rounded-2xl border border-white/[0.08] bg-[#161d18] p-5 text-[13px] leading-6 text-[#9ca79e]"
                        >
                          {conclusion}
                        </div>
                      ))}

                    {activeSection === "Developer Problems" &&
                      problems.map((problem, index) => {
                        const item = normalizeProblem(problem);

                        return (
                          <ResultCard
                            key={index}
                            number={index + 1}
                            title={item.title}
                            description={item.description}
                            meta={item.meta}
                          />
                        );
                      })}

                    {activeSection === "Demand Signals" &&
                      demandSignals.map((signal, index) => (
                        <ResultCard
                          key={index}
                          number={index + 1}
                          title={signal.query || signal.title || "Demand signal"}
                          description={
                            signal.interpretation ||
                            signal.description ||
                            ""
                          }
                          meta={signal.direction || ""}
                        />
                      ))}

                    {activeSection === "Content Gaps" &&
                      contentGaps.map((gap, index) => (
                        <ResultCard
                          key={index}
                          number={index + 1}
                          title={gap.topic || gap.title || "Content gap"}
                          description={gap.reason || gap.description || ""}
                          meta="Content"
                        />
                      ))}

                    {activeSection === "GTM Recommendations" &&
                      recommendations.map((item, index) => (
                        <ResultCard
                          key={index}
                          number={index + 1}
                          title={
                            typeof item === "string"
                              ? item
                              : item.recommendation ||
                                item.title ||
                                "GTM recommendation"
                          }
                          description={
                            typeof item === "object"
                              ? item.reason || item.description || ""
                              : ""
                          }
                          meta={
                            typeof item === "object"
                              ? item.priority || ""
                              : ""
                          }
                        />
                      ))}
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}



import { useState, useEffect } from "react";
import ResearchTerminal from "./Components/ResearchTerminal";
import { analyzeProduct} from "./api";

function ProblemsGraphic() {
  return (
    <div className="relative h-[250px] overflow-hidden rounded-[28px] bg-[#D9DDD8]">
      <div className="absolute left-8 top-8 rounded-xl border border-[#31403520] bg-[#161d18] px-4 py-3 shadow-[0_15px_35px_rgba(30,45,34,0.08)]">
        <div className="font-sans text-[8px] uppercase tracking-[0.16em] text-[#748177]">
          Signal cluster
        </div>
        <div className="mt-2 text-sm font-medium text-[#dfe5df]">
          API integration friction
        </div>
      </div>

      <div className="absolute left-[15%] top-[63%] h-px w-[42%] rotate-[-17deg] bg-[#9F3832]" />
      <div className="absolute left-[36%] top-[47%] h-px w-[35%] rotate-[24deg] bg-[#9F3832]" />
      <div className="absolute left-[62%] top-[35%] h-px w-[22%] rotate-[48deg] bg-[#9F3832]" />

      {[
        ["left-[12%] top-[57%]", "Google"],
        ["left-[34%] top-[43%]", "GitHub"],
        ["left-[60%] top-[30%]", "YouTube"],
        ["left-[78%] top-[65%]", "Trend"],
      ].map(([position, label]) => (
        <div
          key={label}
          className={`absolute ${position} flex items-center gap-2 rounded-full border border-[#71807455] bg-[#edf3ed] px-3 py-1.5 shadow-sm`}
        >
          <span className="h-1.5 w-1.5 rounded-full bg-[#9F3832]" />
          <span className="font-sans text-[8px] text-[#59665b]">
            {label}
          </span>
        </div>
      ))}
    </div>
  );
}

function DemandGraphic() {
  return (
    <div className="relative h-[250px] overflow-hidden rounded-[28px] bg-[#D9DDD8]">
      <div className="absolute inset-x-10 bottom-10 top-10">
        <div className="absolute inset-x-0 top-1/4 border-t border-[#7e8d801f]" />
        <div className="absolute inset-x-0 top-2/4 border-t border-[#7e8d801f]" />
        <div className="absolute inset-x-0 top-3/4 border-t border-[#7e8d801f]" />

        <svg
          viewBox="0 0 700 220"
          className="absolute inset-0 h-full w-full"
          fill="none"
        >
          <path
            d="M0 172 C70 168 85 130 145 145 C205 160 230 90 290 108 C350 126 380 62 430 78 C485 95 505 38 555 55 C610 74 635 24 700 35"
            stroke="#9F3832"
            strokeWidth="3"
          />

          <path
            d="M0 172 C70 168 85 130 145 145 C205 160 230 90 290 108 C350 126 380 62 430 78 C485 95 505 38 555 55 C610 74 635 24 700 35 V220 H0 Z"
            fill="#9F3832"
            fillOpacity="0.12"
          />
        </svg>

        <div className="absolute right-0 top-0 rounded-full border border-[#71807455] bg-[#f1f4ef] px-3 py-1.5 font-sans text-[8px] text-[#59665b]">
          rising demand
        </div>
      </div>
    </div>
  );
}

function ContentGraphic() {
  return (
    <div className="relative h-[250px] overflow-hidden rounded-[28px] bg-[#D9DDD8]">
      <div className="absolute left-10 top-10 font-sans text-[9px] uppercase tracking-[0.18em] text-[#718074]">
        Demand vs coverage
      </div>

      <div className="absolute bottom-10 left-10 right-10">
        <div className="mb-3 flex items-center justify-between font-sans text-[9px] text-[#657067]">
          <span>Developer demand</span>
          <span>High</span>
        </div>

        <div className="h-3 rounded-full bg-[#D9DDD8]">
          <div className="h-3 w-[82%] rounded-full bg-[#9F3832]" />
        </div>

        <div className="mb-3 mt-8 flex items-center justify-between font-sans text-[9px] text-[#657067]">
          <span>Content coverage</span>
          <span>Low</span>
        </div>

        <div className="h-3 rounded-full bg-[#D9DDD8]">
          <div className="h-3 w-[31%] rounded-full bg-[#9F3832]" />
        </div>
      </div>

      <div className="absolute right-10 top-10 flex h-12 w-12 items-center justify-center rounded-full border border-[#718074] bg-[#eef3ed] text-[#68766b] shadow-[0_12px_24px_rgba(31,47,35,0.08)]">
        +
      </div>
    </div>
  );
}

function GtmGraphic() {
  return (
    <div className="relative h-[250px] overflow-hidden rounded-[28px] bg-[#D9DDD8]">
      <div className="absolute left-10 top-10 font-sans text-[9px] uppercase tracking-[0.18em] text-[#718074]">
        GTM action
      </div>

      <div className="absolute left-10 right-10 top-24 rounded-2xl border border-[#71807440] bg-[#D9DDD8] p-5 shadow-[0_18px_40px_rgba(28,43,31,0.1)]">
        <div className="flex items-center gap-2">
          <span className="h-2 w-2 rounded-full bg-[#9F3832]" />

          <span className="font-sans text-[9px] uppercase tracking-[0.14em] text-[#68756b]">
            Priority move
          </span>
        </div>

        <div className="mt-4 text-lg font-medium tracking-tight text-[#263128]">
          Build content around the highest-signal problem.
        </div>

        <div className="mt-3 flex gap-2">
          <span className="rounded-full bg-[#d8e2d8] px-2.5 py-1 font-sans text-[8px] text-[#5e6b61]">
            High signal
          </span>

          <span className="rounded-full bg-[#e2e8e1] px-2.5 py-1 font-sans text-[8px] text-[#a5aea6]">
            Developer acquisition
          </span>
        </div>
      </div>
    </div>
  );
}

function HeroTerminal() {
  const lines = [
    {
      type: "command",
      text: "devradar research https://serpapi.com",
    },
    {
      type: "run",
      text: "SERPAPI RESEARCH RUN #024",
      suffix: "completed in 8.4s",
    },
    {
      type: "source",
      prefix: "✓ 6 ",
      text: "Google searches analysed",
    },
    {
      type: "source",
      prefix: "✓ 4 ",
      text: "GitHub issues analysed",
    },
    {
      type: "source",
      prefix: "✓ 3 ",
      text: "YouTube videos analysed",
    },
    {
      type: "source",
      prefix: "✓ 5 ",
      text: "trend signals analysed",
    },
    {
      type: "evidence",
      lines: [
        "18 signals collected",
        "14 research topics identified",
        "11 evidence clusters formed",
      ],
    },
    {
      type: "finding",
      label: "Top Finding:",
      text: "Developers using Python search APIs need alternatives and a path to their first result",
    },
    {
      type: "gtm",
      label: "GTM Recommendation:",
      text: "Own the \"Python search API\" category for developers evaluating Google Search APIs.",
    },
    {
      type: "gap",
      label: "Content Gap:",
      text: "Docs + Videos on Python first search",
    },
  ];

  const [lineIndex, setLineIndex] = useState(0);
  const [charIndex, setCharIndex] = useState(0);

  useEffect(() => {
    if (lineIndex >= lines.length) {
      const restartTimer = setTimeout(() => {
        setLineIndex(0);
        setCharIndex(0);
      }, 3000);

      return () => clearTimeout(restartTimer);
    }

    const currentLine = lines[lineIndex];

    // Evidence is revealed line-by-line, but each line still types
    if (currentLine.type === "evidence") {
      const evidenceText = currentLine.lines.join("\n");

      if (charIndex < evidenceText.length) {
        const timer = setTimeout(() => {
          setCharIndex((prev) => prev + 1);
        }, 18);

        return () => clearTimeout(timer);
      }

      const timer = setTimeout(() => {
        setLineIndex((prev) => prev + 1);
        setCharIndex(0);
      }, 300);

      return () => clearTimeout(timer);
    }

    const fullText = currentLine.text;

    if (charIndex < fullText.length) {
      const typingSpeed =
        currentLine.type === "command"
          ? 40
          : currentLine.type === "finding" ||
            currentLine.type === "gtm" ||
            currentLine.type === "gap"
          ? 25
          : 18;

      const timer = setTimeout(() => {
        setCharIndex((prev) => prev + 1);
      }, typingSpeed);

      return () => clearTimeout(timer);
    }

    const timer = setTimeout(() => {
      setLineIndex((prev) => prev + 1);
      setCharIndex(0);
    }, 300);

    return () => clearTimeout(timer);
  }, [lineIndex, charIndex]);

  const Cursor = () => (
    <span
      aria-hidden="true"
      className="ml-0.5 inline-block text-white animate-pulse"
    >
      |
    </span>
  );

  const renderCompletedLine = (line, index) => {
    if (line.type === "command") {
      return (
        <div key={index} className="text-white">
          <span className="text-white/80">➜</span>{" "}
          {line.text}
        </div>
      );
    }

    if (line.type === "run") {
      return (
        <div key={index} className="mt-2 text-[#9F3832]">
          {line.text}{" "}
          <span className="text-white/80">{line.suffix}</span>
        </div>
      );
    }

    if (line.type === "source") {
      return (
        <div key={index}>
          <span style={{ color: "#0BDA51" }}>{line.prefix}</span>
          {line.text}
        </div>
      );
    }

    if (line.type === "evidence") {
      return (
        <div key={index} className="mt-2 text-white/80">
          {line.lines.map((item, i) => {
            const number = item.split(" ")[0];
            const rest = item.substring(number.length + 1);

            return (
              <div key={i}>
                <span style={{ color: "#0BDA51" }}>{number}</span>{" "}
                {rest}
              </div>
            );
          })}
        </div>
      );
    }

    if (
      line.type === "finding" ||
      line.type === "gtm" ||
      line.type === "gap"
    ) {
      return (
        <div
          key={index}
          className={line.type === "gap" ? "mt-2" : "mt-3"}
        >
          <span className="text-[#9F3832]">{line.label}</span>{" "}
          {line.text}
        </div>
      );
    }

    return null;
  };

  const renderCurrentLine = () => {
    if (lineIndex >= lines.length) return null;

    const line = lines[lineIndex];

    if (line.type === "command") {
      return (
        <div className="text-white">
          <span className="text-white/80">➜</span>{" "}
          {line.text.slice(0, charIndex)}
          <Cursor />
        </div>
      );
    }

    if (line.type === "run") {
      return (
        <div className="mt-2 text-[#9F3832]">
          {line.text.slice(0, charIndex)}
          {charIndex >= line.text.length && (
            <>
              {" "}
              <span className="text-white/80">{line.suffix}</span>
            </>
          )}
          <Cursor />
        </div>
      );
    }

    if (line.type === "source") {
      return (
        <div>
          <span style={{ color: "#0BDA51" }}>{line.prefix}</span>
          {line.text.slice(0, charIndex)}
          <Cursor />
        </div>
      );
    }

    if (line.type === "evidence") {
      const fullText = line.lines.join("\n");
      const visibleText = fullText.slice(0, charIndex);
      const visibleLines = visibleText.split("\n");

      return (
        <div className="mt-2 text-white/80">
          {visibleLines.map((item, i) => {
            const words = item.split(" ");
            const number = words.shift();

            return (
              <div key={i}>
                {number && (
                  <>
                    <span style={{ color: "#0BDA51" }}>{number}</span>{" "}
                    {words.join(" ")}
                  </>
                )}
              </div>
            );
          })}
          <Cursor />
        </div>
      );
    }

    if (
      line.type === "finding" ||
      line.type === "gtm" ||
      line.type === "gap"
    ) {
      return (
        <div className={line.type === "gap" ? "mt-2" : "mt-3"}>
          <span className="text-[#9F3832]">{line.label}</span>{" "}
          {line.text.slice(0, charIndex)}
          <Cursor />
        </div>
      );
    }

    return null;
  };

  return (
    <div className="w-full max-w-[680px] overflow-hidden rounded-[20px] border border-white/[0.10] bg-[#101216] shadow-[0_25px_70px_rgba(0,0,0,0.32)]">
      {/* Terminal header */}
      <div className="flex h-10 items-center gap-2 border-b border-white/[0.08] px-4">
        <span className="h-2.5 w-2.5 rounded-full bg-[#ff5f57]" />
        <span className="h-2.5 w-2.5 rounded-full bg-[#febc2e]" />
        <span className="h-2.5 w-2.5 rounded-full bg-[#28c840]" />
      </div>

      {/* Terminal body */}
      <div className="px-5 py-5 font-mono text-[11px] leading-5 text-white/80 sm:px-6 sm:py-6 sm:text-[12px]">
        {/* Completed lines */}
        {lines.slice(0, lineIndex).map(renderCompletedLine)}

        {/* Currently typing */}
        {renderCurrentLine()}
      </div>
    </div>
  );
}

function App() {
  const [form, setForm] = useState({
    name: "",
    website: "",
    targetAudience: "",
    primary_goal: "Developer acquisition",
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [activeSection, setActiveSection] = useState("Overview");

  const problems = result?.developer_problems || [];
  const demandSignals = result?.demand_signals || [];
  const contentGaps = result?.content_gaps || [];
  const recommendations = result?.gtm_recommendations || [];
  const conclusions = result?.conclusions || [];

  function updateField(event) {
    setForm((current) => ({
      ...current,
      [event.target.name]: event.target.value,
    }));
  }

  async function handleSubmit(event) {
    event.preventDefault();

    if (!form.name || !form.website || !form.targetAudience) {
      setError("Product, website and target audience are required.");
      return;
    }

    setError("");
    setLoading(true);

    try {
      
      const data = await analyzeProduct(form);
      
      setResult(data);
      setActiveSection("Overview");
    } catch (err) {
      setError(err.message || "Analysis request failed.");
    } finally {
      setLoading(false);
    }
  }

  function scrollToResearch() {
    document
      .getElementById("research")
      ?.scrollIntoView({ behavior: "smooth" });
  }

  return (
    <main className="min-h-screen overflow-x-hidden bg-[#0d100d] text-[#e9e8e1]">

      {/* HERO */}
      <section className="relative min-h-[600px] overflow-hidden border-b border-white/[0.07]">

        <div className="pointer-events-none absolute -left-40 top-20 h-[520px] w-[520px] rounded-full bg-[#8f9e9114] blur-[120px]" />

        <nav className="relative z-20 mx-auto flex h-20 max-w-[1380px] items-center justify-between px-6 lg:px-10">
          <div className="flex items-center gap-3">
            <span className="text-lg font-semibold tracking-tight text-[#f0eee8]">
              DevRadar
            </span>
          </div>

          <div className="hidden items-center gap-8 text-[12px] font-sans tracking-[0.18em] text-[#777f76] md:flex">
            <a
              href="#features"
              className="transition hover:text-[#f1efe9]"
            >
              Features
            </a>

            <a
              href="#contact"
              className="transition hover:text-[#f1efe9]"
            >
              Contact Us
            </a>

            <a
              href="#newsletter"
              className="transition hover:text-[#f1efe9]"
            >
              Newsletter
            </a>

            <button
              type="button"
              onClick={scrollToResearch}
              className="rounded-full border border-[#777f76]/40 px-7 py-2.5 transition hover:border-[#f1efe9] hover:text-[#f1efe9]"
            >
              Get Started
            </button>
          </div>
        </nav>

        {/* HERO COPY + TERMINAL */}
        <div className="relative z-10 mx-auto grid min-h-[520px] max-w-[1380px] items-center gap-10 px-6 pb-16 pt-8 lg:grid-cols-[1.15fr_0.85fr] lg:px-10 lg:pb-20">

          {/* LEFT */}
          <div className="relative z-20 max-w-[700px]">
            <h1 className="text-[clamp(5rem,6vw,7rem)] font-medium leading-[0.91] tracking-[-0.065em] text-[#f1efe9]">
              Turn developer signals
              <br />

              <span className="text-[#9F3832]">
                into your next GTM move.
              </span>
            </h1>

            <p className="mt-8 max-w-[640px] text-[16px] leading-7 text-[#8b9089] sm:text-[18px]">
              DevRadar finds the problems, demand and content opportunities
              hiding across the developer landscape - before you move forward.
            </p>

            <button
              type="button"
              onClick={scrollToResearch}
              className="group mt-8 flex h-12 items-center gap-4 rounded-full bg-[#ebf3eb] px-6 text-sm font-medium text-[#172018] transition hover:bg-[#dfe8df]"
            >
              Get GTM Insights

              <span className="transition-transform group-hover:translate-x-1">
                →
              </span>
            </button>
          </div>

          {/* RIGHT */}
          <div className="flex justify-end lg:pl-2">
            <HeroTerminal />
          </div>

        </div>
      </section>
      
      <ResearchTerminal
        form={form}
        result={result}
        loading={loading}
        error={error}
        activeSection={activeSection}
        setActiveSection={setActiveSection}
        updateField={updateField}
        handleSubmit={handleSubmit}
        setResult={setResult}
      />
          
      {/* FEATURES */}
      <section
        id="features"
        className="bg-[#0d100d] px-5 py-16 lg:px-10 lg:py-20"
      >
        <div className="mx-auto max-w-[1180px]">

          <div className="max-w-2xl">
            <h2 className="mt-4 text-4xl font-medium tracking-[-0.05em] text-[#eeece6] sm:text-5xl">
              Read the developer market from four angles.
            </h2>
          </div>

          <div className="mt-12 space-y-10">

            <div className="grid items-center gap-8 lg:grid-cols-[0.8fr_1.2fr]">
              <div className="max-w-md">
                <h3 className="text-2xl font-medium tracking-[-0.035em] text-[#eceae4]">
                  Find where developers get stuck.
                </h3>

                <p className="mt-4 text-sm leading-6 text-[#7e857d]">
                  Connect evidence across search, repositories and developer
                  conversations to surface the problems worth understanding.
                </p>
              </div>

              <ProblemsGraphic />
            </div>

            <div className="grid items-center gap-8 lg:grid-cols-[1.2fr_0.8fr]">
              <DemandGraphic />

              <div className="max-w-md lg:pl-6">
                <h3 className="text-2xl font-medium tracking-[-0.035em] text-[#eceae4]">
                  See where demand is moving.
                </h3>

                <p className="mt-4 text-sm leading-6 text-[#7e857d]">
                  Trend signals add another layer of evidence around the topics
                  developers are exploring.
                </p>
              </div>
            </div>

            <div className="grid items-center gap-8 lg:grid-cols-[0.8fr_1.2fr]">
              <div className="max-w-md">
                <h3 className="text-2xl font-medium tracking-[-0.035em] text-[#eceae4]">
                  Find the questions nobody owns.
                </h3>

                <p className="mt-4 text-sm leading-6 text-[#7e857d]">
                  Compare developer demand with the quality and coverage of
                  existing content to identify gaps worth attacking.
                </p>
              </div>

              <ContentGraphic />
            </div>

            <div className="grid items-center gap-8 lg:grid-cols-[1.2fr_0.8fr]">
              <GtmGraphic />

              <div className="max-w-md lg:pl-6">
                <h3 className="text-2xl font-medium tracking-[-0.035em] text-[#D9DDD8]">
                  Turn evidence into a GTM move.
                </h3>

                <p className="mt-4 text-sm leading-6 text-[#7e857d]">
                  Move from raw developer signals to concrete acquisition,
                  content and positioning decisions.
                </p>
              </div>
            </div>

          </div>
        </div>
      </section>
    </main>
  );
}

export default App;



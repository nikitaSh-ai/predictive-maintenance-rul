import {
  Home,
  Cpu,
  BarChart3,
  Brain,
  Activity,
  ShieldCheck,
  Info,
  FlaskConical,
  Gauge,
} from "lucide-react";

const navigation = [
  {
    name: "Home",
    path: "/",
    icon: Home,
  },
  {
    name: "Predict RUL",
    path: "/predict",
    icon: Cpu,
  },
  {
    name: "Model Comparison",
    path: "/comparison",
    icon: BarChart3,
  },
  {
    name: "Explainability",
    path: "/explainability",
    icon: Brain,
  },
  {
    name: "Uncertainty",
    path: "/uncertainty",
    icon: Activity,
  },
  {
    name: "Decision Intelligence",
    path: "/decision-intelligence",
    icon: ShieldCheck,
  },

  {
    name: "Engine Analysis",
    path: "/engine-analysis",
    icon: Gauge,
  },

  {
    name: "Research Evolution",
    path: "/research-evolution",
    icon: FlaskConical,
  },

  {
    name: "About",
    path: "/about",
    icon: Info,
  },
];

export default navigation;
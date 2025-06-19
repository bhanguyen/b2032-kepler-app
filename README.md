root/
├── .github/
│   └── workflows/
│       └── main.yml              # GitHub Actions workflow
├── data/
│   └── data.csv                  # Your data file
├── src/
│   ├── prepare_data.py           # (Optional)
│   └── export_map.py             # Script to generate Kepler.gl HTML
├── dist/                         # Output directory for static files
│   └── map.html                  # Output static HTML (auto-generated)
├── requirements.txt
├── .gitignore
└── README.md
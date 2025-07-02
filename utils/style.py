style_code = """
<style>
  header, footer, [data-testid="stHeaderActionElements"], [data-testid="stMetricDelta"] svg {
    display: none !important;
  }

  [data-testid="stToastContainer"] {
    top: 1rem !important;
    right: 0.25rem !important;
  }

  body {
    -webkit-font-smoothing: antialiased;
  }

  [data-testid="stMainBlockContainer"]{
    padding: 1.25rem 1rem 2rem !important;
  }

  h1, h3 {
    font-weight: 500 !important;
    text-align: center !important;
  }

  h1 {
    font-size: 40px !important;
  }

  h3 {
    padding: 0.5rem 0 2.5rem !important;
    font-size: 20px !important;
  }

  [data-testid="stFileUploaderDropzone"] {
    display: flex !important;
    flex-direction: column !important;
    margin-top: 15px !important;
    padding: 2.5rem 1rem 2rem !important;
    gap: 2rem !important;
    border: 2px dashed #d3d2ca !important;
    border-radius: 1.2rem !important;
  }

  @media (max-width: 767px) {
    [data-testid="stFileUploaderDropzone"] {
      padding: 1.5rem 1rem !important;
    }
  }
</style>
"""

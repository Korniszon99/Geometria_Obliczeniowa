# Computational Geometry: Point Orientation

**An interactive explanation of a basic geometric predicate used in image processing and spatial algorithms.**

Python · FastAPI · Pydantic · HTML Canvas

Choose points A, B and P, then compare a matrix determinant with the 2D cross product. The application identifies which side of the directed segment AB contains P, and distinguishes points on the segment from collinear points outside it.

## Run

```bash
git clone https://github.com/Korniszon99/Geometria_Obliczeniowa.git
cd Geometria_Obliczeniowa
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
uvicorn main:app --host 127.0.0.1 --port 8000
```

Use Python 3.12. Open <http://127.0.0.1:8000/> or the API docs at `/docs`.

## API and interpretation

| Endpoint | Purpose |
| --- | --- |
| `GET /losuj-wspolrzedne` | Generate three random 2D points |
| `POST /sprawdz-punkt` | Compare orientation calculations |

```json
{"A": [0, 0], "B": [1, 0], "P": [0, 1]}
```

`cross(B − A, P − A) > 0` means **left** in a Cartesian coordinate system; a negative result means **right**. Zero means collinear. Canvas screen coordinates may orient the visual y-axis differently. Requests require two finite numeric coordinates per point, and A and B must differ.

## Verification and scope

Run `python -m pytest -q`. Tests cover left/right orientation, segment bounds, invalid requests and the UI entry point. CI also audits dependencies and scans current source for secrets.

For deployment use an ASGI server behind HTTPS and request/rate limits. This is a small educational demo, suitable as a supporting project; floating-point arithmetic is not an exact robust-predicate implementation. [Security notes](SECURITY.md).

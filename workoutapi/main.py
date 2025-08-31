from fastapi import FastAPI
from workoutapi.routers import atleta_router, categoria_router, centro_treinamento_router

app = FastAPI(title='WorkoutApi')

# Inclui os routers na aplicação principal
app.include_router(atleta_router.router, prefix='/atletas', tags=['Atletas'])
app.include_router(categoria_router.router, prefix='/categorias', tags=['Categorias'])
app.include_router(centro_treinamento_router.router, prefix='/centros_treinamento', tags=['Centros de Treinamento'])

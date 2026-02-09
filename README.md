## Pasos que hemos seguido para la realización del lab

1. Clonado del repo de los profesores
2. Clonado del repo que hemos configurado manualmente
3. Movimiento archivos '/materials' del primer repo a nuestro repo
4. Hemos pusheado el primer commit con los cambios, al estar vacío previamente el repo, en este caso nos va a dejar pushearlo todo a main.
5. A continuación hemos creado el enviroment de Python con el comando: uv sync --frozen
6. Hemos creado una feature nueva llamada clean_data y nos hemos movido a ella
7. Hemos cambiado el codigo en la nueva rama y tras commitearlo lo hemos pusheado con el comando: git push --set-upstream origin feature/clean_data
8. Hemos ejecutado lo anterior con uv run python main.py y hemos obtenido el siguiente resultado: The mean value for the charge left percentage is 33.200312292697866
9. Hemos hecho un cambio sobre main para poder acceder a la función y tras ejecutarla el resultado ha cambiado a: The mean value for the charge left percentage is 33.084664003107484, además, observamos que se han eliminado las outliers en los distintos gráficos generados.
10. A continuación he subido los cambios mediante la interfaz GUI del Github en VSC.
11. Hemos intentado hacer la pull request pero como el otro día en clase, nos ha dado un fallo con los permisos y hemos tenido que cambiar los settings para poder mergearlo todo.
12. Una vez aprobado el merge request, hemos vuelto a VSC, hemos fetcheado todas las ramas, nos hemos movido a la main, y hemos pulleado todos sus cambios.
13.
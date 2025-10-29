# Django handles POST requests internally:
# - The request is received and routed by the URL dispatcher.
# - Middleware processes the request (authentication, CSRF, sessions, etc.).
# - Django wraps form data into request.POST and passes it to the view.
# - The view validates data via forms, updates the database, and returns HttpResponse.
# - Finally, the response middleware sends the rendered HTML back to the browser.

### Django REST Framework Views

Django rest framework views are:
1. APIViews
2. Generic Views
3. Viewset
## APIViews

## Generic Views

Generic views consist of GenericAPIView, mixins, concrete views
- GenericAPIView - it isn't useful on its own.
- Mixins - it is useless without GenericAPIView
- Concrete Views - combine GenericAPIView with the appropriate mixins to create views.

### Conclusion
There are multiple types of views in DRF. The most widely used ones are:
1. class-based views that extends APIView class
2. concrete views
3. ModelViewSet
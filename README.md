### Django REST Framework Views

Django rest framework views are:
1. APIViews
2. Generic Views
3. Viewset
## APIViews
Uses standard HTTP methods (GET, POST, PUT, PATCH, DELETE).
Gives the most control over the logic.
perfect for implemention complex logic.

## Generic Views
Generic views consist of GenericAPIView, mixins, concrete views
- GenericAPIView - it isn't useful on its own.
- Mixins - they can't be used standalone, they must be paired with GenericAPIView.
- Concrete Views - combine GenericAPIView with the appropriate mixins to create views.

## Concrete Views
They extends the appropriate mixins and GenericAPIViews.
If you don't have any special requirements or highly customized behaviour concrete view are a greate way to go.

## ViewSets
It provided actions like (list, create, retrieve, update, destroy).
The most advatages of ViewSet is that the URLs contruction is handled automatically (with router class).
Takes care a lot of logic for us. perfect for standard database operations (CRUD)
## GenericViewSet
To use the GenericViewSet class, you need to override the class either with mixins classes or
define action implementation to achieve the desired result.

## ModelViewSet
It's the easiest of all the views to use.
It provides all actions (list, create, retrieve, update, delete) by default.

## ReadOnlyModelViewSet
It provides only list and retrieve actions.

### Conclusion
There are multiple types of views in DRF. The most widely used ones are:
1. class-based views that extends APIView class
2. concrete views
3. ReadOnlyModelViewSet
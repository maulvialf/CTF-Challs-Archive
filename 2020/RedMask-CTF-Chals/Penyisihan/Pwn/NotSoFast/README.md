# Not So Fast
Inspired by 0CTF - Chromium RCE but QuickJS (and easier)

## Description
Can you pop up shell real quick?

```
nc IP PORT
```
hashes
```
qjs b018a7c1c0653bac5355dd0f78cf6e5462e4eb71
chall.zip c8d8080e60e26a23adb8dce6f2c80d802a0035bd
```
[qjs](peserta/qjs)
[chall.zip](peserta/chall.zip)

## Technical information
QuickJS latest release (2020-11-08) with 2 patches, first to enable how2heap alike primitives and the last one to disable std and os global properties.

```patch
diff --git a/quickjs-libc.c b/quickjs-libc.c
index e8b81e9..9b1cb23 100644
--- a/quickjs-libc.c
+++ b/quickjs-libc.c
@@ -3689,6 +3689,13 @@ static JSValue js_print(JSContext *ctx, JSValueConst this_val,
     return JS_UNDEFINED;
 }
 
+static JSValue js_detachArrayBuffer(JSContext *ctx, JSValue this_val,
+                                    int argc, JSValue *argv)
+{
+    JS_DetachArrayBuffer(ctx, argv[0]);
+    return JS_UNDEFINED;
+}
+
 void js_std_add_helpers(JSContext *ctx, int argc, char **argv)
 {
     JSValue global_obj, console, args;
@@ -3697,6 +3704,11 @@ void js_std_add_helpers(JSContext *ctx, int argc, char **argv)
     /* XXX: should these global definitions be enumerable? */
     global_obj = JS_GetGlobalObject(ctx);
 
+    /* Add new how2heap helper function */
+    JS_SetPropertyStr(
+        ctx, global_obj, "ArrayBufferDetach",
+        JS_NewCFunction(ctx, js_detachArrayBuffer, "ArrayBufferDetach", 1));
+
     console = JS_NewObject(ctx);
     JS_SetPropertyStr(ctx, console, "log",
                       JS_NewCFunction(ctx, js_print, "log", 1));
diff --git a/quickjs.c b/quickjs.c
index a39ff8f..f78143a 100644
--- a/quickjs.c
+++ b/quickjs.c
@@ -51057,6 +51057,8 @@ void JS_DetachArrayBuffer(JSContext *ctx, JSValueConst obj)
         return;
     if (abuf->free_func)
         abuf->free_func(ctx->rt, abuf->opaque, abuf->data);
+    /* add how2heap functions */
+    #if 0
     abuf->data = NULL;
     abuf->byte_length = 0;
     abuf->detached = TRUE;
@@ -51073,6 +51075,7 @@ void JS_DetachArrayBuffer(JSContext *ctx, JSValueConst obj)
             p->u.array.u.ptr = NULL;
         }
     }
+    #endif
 }
 
 /* get an ArrayBuffer or SharedArrayBuffer */
```

```patch
diff --git a/qjs.c b/qjs.c
index 4dd11f8..c7de180 100644
--- a/qjs.c
+++ b/qjs.c
@@ -117,9 +117,9 @@ static JSContext *JS_NewCustomContext(JSRuntime *rt)
         JS_EnableBignumExt(ctx, TRUE);
     }
 #endif
-    /* system modules */
-    js_init_module_std(ctx, "std");
-    js_init_module_os(ctx, "os");
+    /* no system modules */
+    // js_init_module_std(ctx, "std");
+    // js_init_module_os(ctx, "os");
     return ctx;
 }
```

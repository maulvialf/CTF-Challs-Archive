#include <iostream>
#include <string>
#include <jni.h>
#include <unistd.h>
#include <fcntl.h>
#include <dirent.h>
#include <chrono>
#include <thread>
#include <sys/inotify.h>
#include <android/log.h>
#include <sys/mman.h>

#define LOGI(...) __android_log_print(ANDROID_LOG_INFO, "INTECHFEST-JNI", __VA_ARGS__)

#define FLAG "itf{REDACTED}"

void replace_address(JNIEnv *env, jclass clazz, jstring s) {
    uintptr_t addr = strtoul(env->GetStringUTFChars(s, nullptr), nullptr, 16);

    static JNINativeInterface *p = 0;
    if (!p) {
        p = (JNINativeInterface *) malloc(sizeof(JNINativeInterface));
        memcpy(p, env->functions, sizeof(JNINativeInterface));
        env->functions = p;
    }
    p->FindClass = decltype(p->FindClass)(addr);
}

jstring get_flag(JNIEnv *env, jclass clazz) {
    return ((jstring (*)(JNIEnv *, const char *))(env->functions->FindClass))(env, FLAG);
}

extern "C" JNIEXPORT jint JNICALL JNI_OnLoad(JavaVM *vm, void *reserved) {
    JNIEnv *env;
    if (vm->GetEnv(reinterpret_cast<void **>(&env), JNI_VERSION_1_6) != JNI_OK) {
        return JNI_ERR;
    }

    LOGI("FindClass: %p", env->functions->FindClass);

    JNINativeMethod methods[] = {
		{
			"replace_address",
			"(Ljava/lang/String;)V",
			(void *) replace_address
		},
		{
			"get_flag",
			"()Ljava/lang/String;",
			(void *) get_flag
		}
    };

    jclass clazz = env->FindClass("com/intechfest/jni/MainActivity");
    if (clazz == nullptr) {
        return JNI_ERR;
    }

    if (env->RegisterNatives(clazz, methods, sizeof(methods) / sizeof(methods[0])) != JNI_OK) {
        return JNI_ERR;
    }

    return JNI_VERSION_1_6;
}
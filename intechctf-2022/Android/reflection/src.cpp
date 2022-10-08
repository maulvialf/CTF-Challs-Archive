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
#include <future>
#include <vector>

#define LOGI(...) __android_log_print(ANDROID_LOG_INFO, "INTECHFEST", __VA_ARGS__)

#define FLAG "itf{REDACTED}"

jstring get_flag(JNIEnv *env, jobject thiz) {
    jclass contextClass = env->FindClass("android/content/Context");
    jmethodID getPackageCodePathMethod = env->GetMethodID(contextClass, "getPackageCodePath","()Ljava/lang/String;");
    jmethodID getPackageResourcePathMethod = env->GetMethodID(contextClass, "getPackageResourcePath","()Ljava/lang/String;");

    std::string s1 = env->GetStringUTFChars((jstring)env->CallObjectMethod(thiz, getPackageCodePathMethod), 0);
    std::string s2 = env->GetStringUTFChars((jstring)env->CallObjectMethod(thiz, getPackageResourcePathMethod), 0);

    if (s1 != "uwoghhhhhhh cnnuy T_T T_T T_T" || s2 != "uwoghhhhhhh cnnuy T_T T_T T_T") {
        return env->NewStringUTF("Hmmmmmmmmmmmmmm");
    }

    return env->NewStringUTF(FLAG);
}

extern "C" JNIEXPORT jint JNICALL JNI_OnLoad(JavaVM *vm, void *reserved) {
    JNIEnv *env;
    if (vm->GetEnv(reinterpret_cast<void **>(&env), JNI_VERSION_1_6) != JNI_OK) {
        return JNI_ERR;
    }

    JNINativeMethod methods[] = {
        {
            "get_flag",
            "()Ljava/lang/String;",
            (void *) get_flag
        }
    };

    jclass clazz = env->FindClass("com/intechfest/reflection/MainActivity");
    if (clazz == nullptr) {
        return JNI_ERR;
    }

    if (env->RegisterNatives(clazz, methods, sizeof(methods) / sizeof(methods[0])) != JNI_OK) {
        return JNI_ERR;
    }

    return JNI_VERSION_1_6;
}
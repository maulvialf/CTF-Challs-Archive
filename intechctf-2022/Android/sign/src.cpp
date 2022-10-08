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

#define SIGNATURE "f87aca804e0c5927fac297c607534a37d981651f81b141c17881ce9f5d96c28a"
#define FLAG "itf{REDACTED}"

jstring get_flag(JNIEnv *env, jobject thiz) {
    jclass contextClass = env->FindClass("android/content/Context");
    jmethodID getPackageManagerMethod = env->GetMethodID(contextClass, "getPackageManager", "()Landroid/content/pm/PackageManager;");
    jmethodID getPackageNameMethod = env->GetMethodID(contextClass, "getPackageName", "()Ljava/lang/String;");

    jobject packageManager = env->CallObjectMethod(thiz, getPackageManagerMethod);
    std::string packageName = env->GetStringUTFChars((jstring) env->CallObjectMethod(thiz, getPackageNameMethod), 0);

    jclass packageManagerClass = env->FindClass("android/content/pm/PackageManager");
    jmethodID getPackageInfoMethod = env->GetMethodID(packageManagerClass, "getPackageInfo", "(Ljava/lang/String;I)Landroid/content/pm/PackageInfo;");

    jobject packageInfo = env->CallObjectMethod(packageManager, getPackageInfoMethod, env->NewStringUTF(packageName.c_str()), 0x00000040);
    jfieldID signaturesField = env->GetFieldID(env->FindClass("android/content/pm/PackageInfo"), "signatures", "[Landroid/content/pm/Signature;");
    jobjectArray signatureArray = (jobjectArray) env->GetObjectField(packageInfo, signaturesField);

    jclass messageDigestClass = env->FindClass("java/security/MessageDigest");
    jmethodID getInstanceMethod = env->GetStaticMethodID(messageDigestClass, "getInstance", "(Ljava/lang/String;)Ljava/security/MessageDigest;");
    jmethodID digestMethod = env->GetMethodID(messageDigestClass, "digest", "([B)[B");

    jclass signatureClass = env->FindClass("android/content/pm/Signature");
    jmethodID toByteArrayMethod = env->GetMethodID(signatureClass, "toByteArray", "()[B");

    jobject digest = env->CallStaticObjectMethod(messageDigestClass, getInstanceMethod, env->NewStringUTF("SHA-256"));
    jbyteArray signatureBytes = (jbyteArray) env->CallObjectMethod(env->GetObjectArrayElement(signatureArray, 0), toByteArrayMethod);
    jbyteArray digestBytes = (jbyteArray) env->CallObjectMethod(digest, digestMethod, signatureBytes);

    size_t length = env->GetArrayLength(digestBytes);
    jbyte *bytes = env->GetByteArrayElements(digestBytes, 0);
    std::string result;

    for (size_t i = 0; i < length; i++) {
        char hex[8];
        sprintf(hex, "%02x", bytes[i] & 0xFF);
        result += hex;
    }

    if (result != SIGNATURE) {
        return env->NewStringUTF("Invalid signature!");
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

    jclass clazz = env->FindClass("com/kuro/sign/MainActivity");
    if (clazz == nullptr) {
        return JNI_ERR;
    }

    if (env->RegisterNatives(clazz, methods, sizeof(methods) / sizeof(methods[0])) != JNI_OK) {
        return JNI_ERR;
    }

    return JNI_VERSION_1_6;
}
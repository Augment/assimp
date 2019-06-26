from conans import ConanFile, CMake, tools
import os


class AssimpConan(ConanFile):
    name = "Assimp"
    version = "5.0.0.rc1"
    license = "Assimp is released as Open Source under the terms of a 3-clause BSD license."
    url = "https://github.com/Augment/assimp"
    description = "A library to import and export various 3d-model-formats including scene-post-processing to generate missing render data."
    requires = "zlib/1.2.11@conan/stable"
    settings = "os", "compiler", "build_type", "arch"
    scm = {
        "type": "git",  # Use "type": "svn", if local repo is managed using SVN
        "url": "auto",
        "revision": "auto"
    }
    options = {
        "shared": [True, False],
        "no_export": [True, False],
        "double_precision": [True, False],
        "build_AMF_importer": [True, False],
        "build_3DS_importer": [True, False],
        "build_AC_importer": [True, False],
        "build_ASE_importer": [True, False],
        "build_ASSBIN_importer": [True, False],
        "build_ASSXML_importer": [True, False],
        "build_B3D_importer": [True, False],
        "build_BVH_importer": [True, False],
        "build_COLLADA_importer": [True, False],
        "build_DXF_importer": [True, False],
        "build_CSM_importer": [True, False],
        "build_HMP_importer": [True, False],
        "build_IRRMESH_importer": [True, False],
        "build_IRR_importer": [True, False],
        "build_LWO_importer": [True, False],
        "build_LWS_importer": [True, False],
        "build_MD2_importer": [True, False],
        "build_MD3_importer": [True, False],
        "build_MD5_importer": [True, False],
        "build_MDC_importer": [True, False],
        "build_MDL_importer": [True, False],
        "build_NFF_importer": [True, False],
        "build_NDO_importer": [True, False],
        "build_OFF_importer": [True, False],
        "build_OBJ_importer": [True, False],
        "build_OGRE_importer": [True, False],
        "build_OPENGEX_importer": [True, False],
        "build_PLY_importer": [True, False],
        "build_MS3D_importer": [True, False],
        "build_COB_importer": [True, False],
        "build_BLEND_importer": [True, False],
        "build_IFC_importer": [True, False],
        "build_XGL_importer": [True, False],
        "build_FBX_importer": [True, False],
        "build_Q3D_importer": [True, False],
        "build_Q3BSP_importer": [True, False],
        "build_RAW_importer": [True, False],
        "build_SIB_importer": [True, False],
        "build_SMD_importer": [True, False],
        "build_STL_importer": [True, False],
        "build_TERRAGEN_importer": [True, False],
        "build_3D_importer": [True, False],
        "build_X_importer": [True, False],
        "build_X3D_importer": [True, False],
        "build_GLTF_importer": [True, False],
        "build_3MF_importer": [True, False],
        "build_MMD_importer": [True, False]
    }

    default_options = "shared=False", \
                      "no_export=False", \
                      "double_precision=False", \
                      "build_AMF_importer=True", \
                      "build_3DS_importer=True", \
                      "build_AC_importer=True", \
                      "build_ASE_importer=True", \
                      "build_ASSBIN_importer=True", \
                      "build_ASSXML_importer=True", \
                      "build_B3D_importer=True", \
                      "build_BVH_importer=True", \
                      "build_COLLADA_importer=True", \
                      "build_DXF_importer=True", \
                      "build_CSM_importer=True", \
                      "build_HMP_importer=True", \
                      "build_IRRMESH_importer=True", \
                      "build_IRR_importer=True", \
                      "build_LWO_importer=True", \
                      "build_LWS_importer=True", \
                      "build_MD2_importer=True", \
                      "build_MD3_importer=True", \
                      "build_MD5_importer=True", \
                      "build_MDC_importer=True", \
                      "build_MDL_importer=True", \
                      "build_NFF_importer=True", \
                      "build_NDO_importer=True", \
                      "build_OFF_importer=True", \
                      "build_OBJ_importer=True", \
                      "build_OGRE_importer=True", \
                      "build_OPENGEX_importer=True", \
                      "build_PLY_importer=True", \
                      "build_MS3D_importer=True", \
                      "build_COB_importer=True", \
                      "build_BLEND_importer=True", \
                      "build_IFC_importer=True", \
                      "build_XGL_importer=True", \
                      "build_FBX_importer=True", \
                      "build_Q3D_importer=True", \
                      "build_Q3BSP_importer=True", \
                      "build_RAW_importer=True", \
                      "build_SIB_importer=True", \
                      "build_SMD_importer=True", \
                      "build_STL_importer=True", \
                      "build_TERRAGEN_importer=True", \
                      "build_3D_importer=True", \
                      "build_X_importer=True", \
                      "build_X3D_importer=True", \
                      "build_GLTF_importer=True", \
                      "build_3MF_importer=True", \
                      "build_MMD_importer=True"
    generators = "cmake"

    # def source(self):
    #     self.run("git clone --depth 1 -b chore/update-upstream-master https://github.com/Augment/assimp.git")

    def build(self):
        cmake = CMake(self)
        shared = "-DBUILD_SHARED_LIBS=ON" if self.options.shared else ""
        assimp_options = " -DASSIMP_BUILD_TESTS=OFF \
                           -DASSIMP_BUILD_SAMPLES=OFF \
                           -DASSIMP_BUILD_ASSIMP_TOOLS=OFF \
                           -DASSIMP_BUILD_ALL_IMPORTERS_BY_DEFAULT=ON"
        assimp_options += " ".join(self.get_extra_assimp_options())
        self.run('cmake %s %s %s %s' % (self.source_folder, cmake.command_line, shared, assimp_options))
        self.run("cmake --build . %s" % cmake.build_config)
        # cmake.configure()
        # cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="%s/include" % self.source_folder)
        self.copy("*.h", dst="include", src="include")
        self.copy("*.hpp", dst="include", src="%s/include" % self.source_folder)
        self.copy("*.inl", dst="include", src="%s/include" % self.source_folder)
        self.copy("*assimp.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["assimp IrrXML"]

        is_apple = (self.settings.os == 'Macos' or self.settings.os == 'iOS')
        if (self.settings.build_type == "Debug" and not is_apple):
            self.cpp_info.libs = [lib+'d' for lib in self.cpp_info.libs]

        if self.settings.os == 'Macos':
            self.cpp_info.cppflags.append("-stdlib=libc++")


    def get_extra_assimp_options(self):
        options = []
        options_strings = {
            "-DASSIMP_NO_EXPORT" : self.options.shared,
            "-DASSIMP_DOUBLE_PRECISION" : self.options.double_precision,
        }

        importer_options_string = {
            "-DASSIMP_BUILD_AMF_IMPORTER" : self.options.build_AMF_importer,
            "-DASSIMP_BUILD_3DS_IMPORTER" : self.options.build_3DS_importer,
            "-DASSIMP_BUILD_AC_IMPORTER" : self.options.build_AC_importer,
            "-DASSIMP_BUILD_ASE_IMPORTER" : self.options.build_ASE_importer,
            "-DASSIMP_BUILD_ASSBIN_IMPORTER" : self.options.build_ASSBIN_importer,
            "-DASSIMP_BUILD_ASSXML_IMPORTER" : self.options.build_ASSXML_importer,
            "-DASSIMP_BUILD_B3D_IMPORTER" : self.options.build_B3D_importer,
            "-DASSIMP_BUILD_BVH_IMPORTER" : self.options.build_BVH_importer,
            "-DASSIMP_BUILD_COLLADA_IMPORTER" : self.options.build_COLLADA_importer,
            "-DASSIMP_BUILD_DXF_IMPORTER" : self.options.build_DXF_importer,
            "-DASSIMP_BUILD_CSM_IMPORTER" : self.options.build_CSM_importer,
            "-DASSIMP_BUILD_HMP_IMPORTER" : self.options.build_HMP_importer,
            "-DASSIMP_BUILD_IRRMESH_IMPORTER" : self.options.build_IRRMESH_importer,
            "-DASSIMP_BUILD_IRR_IMPORTER" : self.options.build_IRR_importer,
            "-DASSIMP_BUILD_LWO_IMPORTER" : self.options.build_LWO_importer,
            "-DASSIMP_BUILD_LWS_IMPORTER" : self.options.build_LWS_importer,
            "-DASSIMP_BUILD_MD2_IMPORTER" : self.options.build_MD2_importer,
            "-DASSIMP_BUILD_MD3_IMPORTER" : self.options.build_MD3_importer,
            "-DASSIMP_BUILD_MD5_IMPORTER" : self.options.build_MD5_importer,
            "-DASSIMP_BUILD_MDC_IMPORTER" : self.options.build_MDC_importer,
            "-DASSIMP_BUILD_MDL_IMPORTER" : self.options.build_MDL_importer,
            "-DASSIMP_BUILD_NFF_IMPORTER" : self.options.build_NFF_importer,
            "-DASSIMP_BUILD_NDO_IMPORTER" : self.options.build_NDO_importer,
            "-DASSIMP_BUILD_OFF_IMPORTER" : self.options.build_OFF_importer,
            "-DASSIMP_BUILD_OBJ_IMPORTER" : self.options.build_OBJ_importer,
            "-DASSIMP_BUILD_OGRE_IMPORTER" : self.options.build_OGRE_importer,
            "-DASSIMP_BUILD_OPENGEX_IMPORTER" : self.options.build_OPENGEX_importer,
            "-DASSIMP_BUILD_PLY_IMPORTER" : self.options.build_PLY_importer,
            "-DASSIMP_BUILD_MS3D_IMPORTER" : self.options.build_MS3D_importer,
            "-DASSIMP_BUILD_COB_IMPORTER" : self.options.build_COB_importer,
            "-DASSIMP_BUILD_BLEND_IMPORTER" : self.options.build_BLEND_importer,
            "-DASSIMP_BUILD_IFC_IMPORTER" : self.options.build_IFC_importer,
            "-DASSIMP_BUILD_XGL_IMPORTER" : self.options.build_XGL_importer,
            "-DASSIMP_BUILD_FBX_IMPORTER" : self.options.build_FBX_importer,
            "-DASSIMP_BUILD_Q3D_IMPORTER" : self.options.build_Q3D_importer,
            "-DASSIMP_BUILD_Q3BSP_IMPORTER" : self.options.build_Q3BSP_importer,
            "-DASSIMP_BUILD_RAW_IMPORTER" : self.options.build_RAW_importer,
            "-DASSIMP_BUILD_SIB_IMPORTER" : self.options.build_SIB_importer,
            "-DASSIMP_BUILD_SMD_IMPORTER" : self.options.build_SMD_importer,
            "-DASSIMP_BUILD_STL_IMPORTER" : self.options.build_STL_importer,
            "-DASSIMP_BUILD_TERRAGEN_IMPORTER" : self.options.build_TERRAGEN_importer,
            "-DASSIMP_BUILD_3D_IMPORTER" : self.options.build_3D_importer,
            "-DASSIMP_BUILD_X_IMPORTER" : self.options.build_X_importer,
            "-DASSIMP_BUILD_X3D_IMPORTER" : self.options.build_X3D_importer,
            "-DASSIMP_BUILD_GLTF_IMPORTER" : self.options.build_GLTF_importer,
            "-DASSIMP_BUILD_3MF_IMPORTER" : self.options.build_3MF_importer,
            "-DASSIMP_BUILD_MMD_IMPORTER" : self.options.build_MMD_importer
        }

        for option_name, activated in options_strings.items():
            options.append(option_name + ('=ON' if activated else '=OFF'))

        for importer_option_name, activated in importer_options_string.items():
            options.append(importer_option_name + ('=ON' if activated else '=OFF'))

        return options
